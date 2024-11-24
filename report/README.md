# An analysis of Voyager for coding tasks

## TODO: Abstract 
- Skills library has a marginally **negative** effect on performance
- We explain potential reasons why this is the case for coding tasks, despite Voyager's success in Minecraft
- Highlight other limitations of Voyager
- Review existing solutions.
- Suggest ways to improve Voyager for coding tasks.

## Introduction

### Voyager
Voyager `[1]` is an agent architecture set in the Minecraft environment, 
where LLMs are used to learn increasingly complex skills through environment interaction. 

It has these main components:
- `curriculum_agent`: Proposes tasks based on exploration progress
- `action_agent`: Generates code to solve the task via environment execution
- `critic_agent`: Checks task success from environment execution outputs and generates critique
- `skill_manager`: Writes descriptions of skills (code which successfully solves a task) for retrieval during code generation

See the fig below from the paper

![Voyager](./assets/voyager_overview.png)


#### Voyager pseudocode
```python
# Instantiate env, curriculum_agent, action_agent, critic_agent, skill_manager, agent_state

while iteration < max_iterations:
    completed_tasks = curriculum_agent.get_completed_tasks()
    failed_tasks = curriculum_agent.get_failed_tasks()
    exploration_progress = curriculum_agent.get_exploration_progress(completed_tasks, failed_tasks)
    task = curriculum_agent.propose_next_task(agent_state , exploration_progress)
    # instantiate variables code, env_feedback, execution_errors, critique, success

    for i in range(4):
        skills = skill_manager.retrieve_skills(task, env_feedback)
        code = action_agent.generate_code(task, code, env_feedback, execution_errors, critique, skills)
        agent_state, env_feedback, execution_errors = env.step(code)
        success, critique = critic_agent.check_task_success(task, agent_state)
        if success:
            break
    
    if success:
        skill_manager.add_skill(code)
        curriculum_agent.add_completed_task(task)
    else:
        curriculum_agent.add_failed_task(task)
```

#### Voyager outcomes
- Unlocks more items, travels further and unlocks tech tree faster than other agents
- Skills library (code) helps other models perform better

#### Advantages
- Interpretable skills library
- Compositionality: New skills built on top of existing skills (functions calling previously written functions)
- Transferability: Skills can be used by other agents since it is code
- Persistent: Skills are saved and can be used in future sessions, compared to neural networks which might forget when it learns new things

### AI for code
Current experiment: can we reuse Voyager to tackle coding tasks, since it already interfaces with code?

Advantages of Voyager are also relevant to AI for code

## Experiments

### Benchmark
MBPP Plus `[2]` is a coding benchmark based off MBPP `[3]` with more test cases per example, and filtered / edited for correctness.

From the problem statement, the AI is expected to write a function that satisfies the test cases.

### Baselines
- Zero shot pass@1 (see [website](https://evalplus.github.io/leaderboard.html))
- ReAct `[4]` (basically Voyager without skill library)

### Models
- GPT-4-Turbo (Nov 2023) as the baseline large model
    - Why not GPT-4o? See later
- GPT 4o Mini (July 2024) as the baseline smaller model
- Ada 002 embeddings

### Training details
All settings follow the original Voyager paper `[1]` unless otherwise stated
- 100 iterations Voyager training
    - During task proposal, curriculum agent will be warned for proposing an already completed task, up to 5 retry attempts
    - GPT 3.5 1106 cannot propose new tasks beyond 20 iterations
        - even after increasing temperature (up to 1 from default 0.1 in the Voyager paper)
    - 4o mini cannot propose new tasks beyond 80 iterations
    - 4o (Aug 2024) cannot propose new tasks beyond 94 iterations
### Eval details
- Skill library from GPT-4-Turbo (Nov 2023) training is used by both models to run on MBPP Plus
- Each MBPP Plus task comes with one public test case. During evaluation, the for loop in the pseudocode is run for the one public test case and the success is determined by the assertion rather than the critic. The answer at the end of the loop (be it from successsful assertion or all tries) is used for evaluation on the private test cases.

## Results
### Accuracy comparison
![Accuracy comparison](./assets/accuracy_comparison.png)

### Error analysis summary
The table below shows the number of questions that changed outcomes when switching from ReAct to Voyager:

| Change Type | GPT-4o Mini | GPT-4-Turbo |
|------------|-------------|--------------|
| Pass → Fail | 4 | 8 |
| Fail → Pass | 1 | 10 |

**Voyager skills not suited for coding tasks**: Switching from ReAct to Voyager causes a drop in accuracy for 4o mini and only a marginal increase in GPT-4-Turbo. 
- We do not take these numbers directly; In the discussion, we dive into the exact questions and remove those that are invalid / ambiguous. After doing so, we find that the skills library has a marginally negative effect on performance for both models.
- Early experiments with GPT 3.5-1106 as the QA model (used for generating the context) with 4-1106 as the action model resulted in 78.0% accuracy in ReAct, the same as the best current result with Voyager. This suggests that the improvement from the skills library might not be significant.

## Discussion

### ReAct is a strong baseline
The largest gains are from switching from Zero shot to ReAct, boosting accuracies by roughly 4% for both models.

### Error analysis: Deeper dive
In this section, we analyze the questions where ReAct and Voyager differ in their result.
Right to wrong refers to questions where ReAct is right and Voyager is wrong, and vice versa for wrong to right.
We looked through all such questions and state the valid ones 
(those that suggest how the skills library might have an influence on the outcome) here. 
The invalid/ambiguous questions are left in the [appendix](APPENDIX.md).

Note: QA agent is a **smaller model** which
- Self asks and answers questions for context to influence the curriculum agent
- Attempts to answer the task and this is used as context for both coding agent and retrieval (this context seems to influence the coding agent to some degree, which propagates to the error analysis)

#### GPT 4o mini
Right to wrong:
- Mbpp 123: Requires finding divisors of a number. The QA agent suggested the linear way (iterating through all numbers) as context. The ReAct agent did not listen to the context and instead used a more efficient method (iterating only up to the square root of n), while Voyager naively followed the QA agent's context. As a result, Voyager got TLE (MBPP Plus uses a time limit ratio of the reference solution's runtime). The skills retrieved do not seem relevant.

The above suggests that a longer context could have distracted the coding agent from a more efficient solution, but even this is debatable. As such, we conclude that the skills library has a marginally negative (0.3%) effect on performance for this model, but not significant.

#### GPT 4o
Wrong to right:
- 239: Dynamic programming problem which LLMs are known to struggle with. ReAct attempts multiple times but fails all of them, while Voyager retrieves dynamic programming skills and gets it right on the first try. While the skills' dynamic programming substructure is not exactly the same as the question, influencing GPT 4 to get it right on the first try seems like weak positive evidence.
- 451: remove whitespace from a string. QA agent naively replaced ' ' with ''. ReAct realized this and accounted for tabs and newlines, while Voyager blindly followed this. The retrieved skills were not relevant. However, ReAct was marked wrong and Voyager right, when it should be the other way around. This is weak evidence **against** the skill library
- 800: this is a variant of the whitespace question in 451, with the same conclusion (weak evidence **against** the skill library)

Right to wrong
- 232: Get largest n nums in a list. Voyager was influenced by its retrieved skill which used a heap, but failed to handle the edge case of $n=0$, because the skill also did not handle that case. Example of how skills can be bad -- if it is not correctly implemented
- 247: QA agent hallucinated bad and suggested misleading methods. ReAct caught this error n fixed but not Voyager.
- 573: Multiply unique numbers in a list. "Unique" can have 2 meanings: Each number is used once regardless of frequency, or only the numbers that appear once. The right answer uses the former (deduced by QA agent and ReAct). In Voyager, one of the retrieved skills `sum_of_unique_numbers` uses the latter, and influenced Voyager to get it wrong over all tries despite the critic suggesting the right answer!
- 603: Get lucid numbers. QA agent gave wrong answer. ReAct initially got it wrong but corrected itself from the critique. Voyager also went though the same process of refining its solution but could not arrive at the right answer at the end of all tries. Retrieved skills do not seem relevant; Weak evidence that retrieved skills can cause context confusion.
- 781: Similar scenario as Mbpp 123 for 4o mini for getting divisors of a number. Surprisingly, the retrieved skills contain a mix of signals: `count_divisible` linearly iterates through a list while `find_nth_prime` iterates up to the square root of $n$.


In total for GPT 4o, we have 1 point for the skill library and 7 points against it (note that wrong to right for 451 and 800 are also against the skill library). This is effectively a 1.6% decrease in performance.

#### Summary
After filtering for invalid / ambiguous questions, we find that the skills library is slightly detrimental to both models, with GPT 4o mini showing a 0.3% decrease in performance and GPT 4o showing a 1.6% decrease.

Success modes:
- Mild influence towards right answer for dynamic programming

Failure modes:
- Distraction from correcting wrong / inefficient / incomplete solution by QA agent or correction by critic (ReAct can self correct while Voyager did not)
- Flaw in skills influence Voyager to also use the same flaw (232)


### Was there compositional skill learning?
Yes. The only example in GPT 4 where a previous skill was called as a function can be found in task 33:

> Write a Python function that takes a list of integers and returns the sum of the two largest numbers in the list. The function should handle lists with at least two integers and should not modify the original list.
> You must strictly follow the function name: `sum_of_two_largest`

The skills retrieved are `first_recurring_character`, `length_of_lis`, `recursive_sum`, `find_kth_largest`, `bubble_sort`

The solution from the coding agent is:
```python
def sum_of_two_largest(numbers):
    largest = find_kth_largest(numbers, 1)
    second_largest = find_kth_largest(numbers, 2)
    return (largest + second_largest)
```
which uses `find_kth_largest`

```python
import heapq

def find_kth_largest(nums, k):
    min_heap = []
    for num in nums:
        if (len(min_heap) < k):
            heapq.heappush(min_heap, num)
        elif (num > min_heap[0]):
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return heapq.heappop(min_heap)
```

This solution passes the test cases, and is saved in the skill library.

In GPT 4o mini, composition can be found in task 42, while in task 79, composition was attempted but the task was not solved. 
In GPT 4o, no composition was found.

### Were the skills used during testing?
Yes, sort of. In GPT 4, task MBPP 472
> Write a python function to check whether the given list contains consecutive numbers or not.
> ```python
> assert check_Consecutive([1,2,3,4,5]) == True
> ```

The retrieved skills are `has_unique_chars`, `first_recurring_character`, `find_pair_with_sum`, `look_and_say_v2`, `find_peak_element`

The coding agent copied the `has_unique_chars` skill and used it in the solution instead of calling the function directly:

```python
def has_unique_chars(lst):
    seen = set()
    for item in lst:
        if (item in seen):
            return False
        seen.add(item)
    return True




def check_Consecutive(nums):
    if (not nums):
        return False
    min_num = min(nums)
    max_num = max(nums)
    return ((((max_num - min_num) + 1) == len(nums)) and has_unique_chars(nums))
```

The same thing happens in tasks 583 and 592. In GPT 4o mini, it happens in 395, 456, 583.

#### Failure to use skills library
The coding agent might not be using the skills library as effectively. Let's take the example from testing on MBPP Plus.

In Mbpp 274 for GPT 4, the factorial function is in the retrieved skills: `calculate_factorial`, `recursive_sum_v2`, `recursive_sum`, `climb_stairs`, `climb_stairs_v2`

However, the coding agent chose to write its own factorial function in its solution:
```python
def even_binomial_Coeff_Sum(n):

    def factorial(x):
        if (x == 0):
            return 1
        result = 1
        for i in range(1, (x + 1)):
            result *= i
        return result

    def binomial_coefficient(n, k):
        return (factorial(n) // (factorial(k) * factorial((n - k))))
    total_sum = 0
    for k in range(0, (n + 1), 2):
        total_sum += binomial_coefficient(n, k)
    return total_sum
```

It did not mention the retrieved skills during its thought process
```
 Plan:
1) Define the function `even_binomial_Coeff_Sum(n)` that takes a positive integer `n` as an argument.
2) Initialize a variable `total_sum` to 0 to keep track of the sum of the binomial coefficients.
3) Use a for loop to iterate over the even indices from 0 to `n` (inclusive) with a step of 2.
4) For each even index `k`, calculate the binomial coefficient using the formula `C(n, k) = n! / (k! * (n-k)!)`.
5) Add the calculated binomial coefficient to `total_sum`.
6) After the loop, return `total_sum`.

Code:
...

Note: The helper function `factorial` is used to calculate the factorial of a number, which is needed for the binomial coefficient calculation. The helper function `binomial_coefficient` calculates the binomial coefficient using the factorial function. The main function `even_binomial_Coeff_Sum` uses these helper functions to calculate the sum of even index binomial coefficients.
```

showing that it was not influenced by the skills library. 
The same thing happens in GPT 4o mini for task 100.

### Why does the skill library / curriculum not help?

#### Explanation 1: Context length
Voyager uses a retrieval $k=5$ which can cause the context to be quite long.
The coding agent also receives various other info. Here is an example:

System prompt:
```
    You are a helpful assistant that writes python code to solve a task specified by me.

    Here are some useful functions written earlier which you can reuse or reference.


    [Entry]:


        def climb_stairs_v2(n):
            if ((n == 0) or (n == 1)):
                return 1
            dp = ([0] * (n + 1))
            (dp[0], dp[1]) = (1, 1)
            for i in range(2, (n + 1)):
                dp[i] = (dp[(i - 1)] + dp[(i - 2)])
            return dp[n]

    [/Entry]

    [Entry]:


        def climb_stairs(n):
            if ((n == 0) or (n == 1)):
                return 1
            ways = ([0] * (n + 1))
            (ways[0], ways[1]) = (1, 1)
            for i in range(2, (n + 1)):
                ways[i] = (ways[(i - 1)] + ways[(i - 2)])
            return ways[n]

    [/Entry]

    [Entry]:


        def climbing_stairs(n, memo=None):
            if (memo is None):
                memo = {}
            if (n == 0):
                return 1
            if (n < 0):
                return 0
            if (n in memo):
                return memo[n]
            memo[n] = ((climbing_stairs((n - 1), memo) + climbing_stairs((n - 2), memo)) + climbing_stairs((n - 3), memo))
            return memo[n]

    [/Entry]

    [Entry]:


        def fibonacci(n):
            if (n == 0):
                return 0
            elif (n == 1):
                return 1
            else:
                return (fibonacci((n - 1)) + fibonacci((n - 2)))

    [/Entry]

    [Entry]:


        def calculate_factorial(n):
            if (n < 0):
                raise ValueError('Factorial is not defined for negative numbers.')
            if (n == 0):
                return 1
            result = 1
            for i in range(1, (n + 1)):
                result *= i
            return result

    [/Entry]






    At each round of conversation, I will give you
    [Environment feedback] (after executing code) ...
    [Code from the last round] ...
    [Task] ...
    [Context] ...
    [Critique] ...

    You should then respond to me with
    Explain (if applicable): Are there any steps missing in your plan? Why does the code not complete the task? What does the chat log and execution error imply?
    Plan: How to complete the task step by step. 
    Code:
        1) Reuse or reference the above useful programs if necessary.
        2) Your function will be reused for building more complex functions. Therefore, you should make it generic and reusable. 
        3) Functions in the "Code from the last round" section will not be saved or executed. Do not reuse functions listed there.
        4) Anything defined outside a function will be ignored, define all your variables inside your functions.
        5) Do not write infinite loops.
        6) If the task specifies a function name to be used, follow it strictly (be case sensitive!). Else, name your function in a meaningful way (can infer the task from the name).
        7) Your code should only contain elements that solve the task, so DO NOT write any assert statements / tests
        8) The context in the [Context] tag serves as a casual tip (which can be wrong) to help you on the task, but your priority is to follow instructions in the [Task] tag.

    You should only respond in the format as described below:
    RESPONSE FORMAT:

    Explain: ...
    Plan:
    1) ...
    2) ...
    3) ...
    ...
    Code:
    ```python
    # helper functions (only if needed, try to avoid them)
    ...
    # main function after the helper functions
    def yourMainFunctionName(args):
    # ...

    ```

```

Human message:
```
    [Environment feedback]
    Note: Tests are automatically generated and can be wrong.

    Tests passed:
    None

    Tests failed:
    assert eulerian_num(3, 1) == 4 # output: 6

    [Code from the last round]


    def eulerian_num(n, m):
        A = [([0] * (n + 1)) for _ in range((n + 1))]
        A[0][0] = 1
        for i in range(1, (n + 1)):
            A[i][0] = 1
            A[i][i] = 0
        for i in range(1, (n + 1)):
            for j in range(1, i):
                A[i][j] = (((i - j) * A[(i - 1)][j]) + ((j + 1) * A[(i - 1)][(j - 1)]))
        return A[n][m]


    [Task]
    Write a Python function that satisfies the description below. Your code must strictly follow the function name and typings of the input and output specified in the assert statement below, and pass the assertion when executed.
    """
    Write a function to find the Eulerian number a(n, m).
    assert eulerian_num(3, 1) == 4
    """


    [Context]
    Rough plan to accomplish the task (can be wrong): 
    Answer: To find the Eulerian number \( A(n, m) \), which counts the number of permutations of \( n \) elements in which exactly \( m \) elements are greater than the previous element, you can use a recursive approach or dynamic programming.

    Conceptually, the Eulerian number can be defined using the following recurrence relations:

    1. **Base Cases**:
    - \( A(0, 0) = 1 \) (the empty permutation)
    - \( A(n, 0) = 1 \) for \( n > 0 \) (only one way to arrange \( n \) elements with no ascents)
    - \( A(n, n) = 0 \) for \( n > 0 \) (no way to arrange \( n \) elements with \( n \) ascents)

    2. **Recurrence Relation**:
    - For \( n > 0 \) and \( 0 \leq m < n \):
        \[
        A(n, m) = (n - m) \cdot A(n - 1, m) + (m + 1) \cdot A(n - 1, m - 1)
        \]
    This relation combines the cases based on whether the largest element is at the end of the permutation or not.

    To implement this in Python, you can create a function that uses either recursion with memoization or a dynamic programming table to store previously computed values of \( A(n, m) \).

    Here’s a simple outline of how you might implement this:

    ```python
    def eulerian_num(n, m):
        # Create a 2D list to store the values of A(n, m)
        A = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Base cases
        A[0][0] = 1
        for i in range(1, n + 1):
            A[i][0] = 1  # A(n, 0) = 1
            A[i][i] = 0  # A(n, n) = 0
        
        # Fill the table using the recurrence relation
        for i in range(1, n + 1):
            for j in range(1, i):
                A[i][j] = (i - j) * A[i - 1][j] + (j + 1) * A[i - 1][j - 1]
        
        return A[n][m]

    # Example usage
    assert eulerian_num(3, 1) == 4
    ```

    This function initializes a table to store the values of the Eulerian numbers and fills it according to the defined recurrence relations. Finally, it returns the value of \( A(n, m) \).


    [Critique]
    The issue in the implementation is likely due to an off-by-one error in the loop bounds or an incorrect implementation of the recurrence relation. To correct this, ensure that the loop ranges are correct and that the recurrence relation is implemented exactly as defined. Specifically, check the indices used in the recurrence relation and verify that they match the mathematical definition of the Eulerian number.

```

While models do have the context length, 
it is generally not advisable to put too much info in the context as it can cause confusion.
Here are some pieces of evidence:

- `[5]` evaluated language models on computing olympiad problems and found that the optimal retrieval size is 2, and additional retrievals degrade performance.
- `[6]` found that in long context settings, language models attend stronger to the beginning and the end of the context, and weaker to the middle. Having a long context thus risks the important information being "lost in the middle" as their title suggests.
- In early experiments, we added a library of problems and solutions for retrieval, and then also added the Voyager skills library. Both are retrieved with $k=5$. We found that each addition of a library degraded performance for both small and large models.
- The error analysis earlier showed that long context can degrade the LM's ability to self-correct.

#### Explanation 2: Poor code reusability

Voyager stores the entire code that solves the task, which favors reuse if one task is a strict subset of another.
This might be the case for MineCraft tasks, but not so much in coding -- 
A more realistic breakdown of coding tasks is: "Coding tasks have modules in common, but also have unique components".
As such, it might be better to store a subset of the code which solves the task, rather than the entire code.

In fact, `[7]` found that when LLMs transform a dataset of problems and solutions by modularizing the code, the in-context learning performance when using the modular code is better compared to using the original dataset.

#### Explanation 3: Poor curriculum variety

As mentioned earlier, LLMs struggle to produce diverse tasks, which limits the variety of skills that can be learned.
Furthermore, if skills are similar, retrievals will be similar which limits the coding agent.
- In fact, we can reference the system prompt previously shown: It retrieved 3 skills that are variations of `climbing_stairs`.
- There are 19 instances of `v2` skills (when the curriculum agent proposes a task which ground truth function name collides with a skill in the skill library, we append `v2` to the function name) in our skill library.
- In the original Voyager repo (for Minecraft), the skills library from the 3 trials had 12/57, 10/57 and 11/58 `v2` (or higher) skills respectively which suggest that the problem of proposing similar task names (and thus similar tasks) is not unique to the coding environment.
- Even for the successful training run with GPT 4, we see that the warning for proposing a task that has already been completed is triggered 10 times.

### Other curriculum limitations
- The prompt for proposing new tasks contains the **entire history** of completed and failed tasks, limiting its scalability -- eventually the maximum context length will be reached. Even before that, the prompt will become too long and which is not good as discussed earlier. This might also explain why the curriculum agent has tendencies to propose completed tasks despite the task being displayed in the prompt -- Lost in the middle effects `[6]`.
- Using LMs to propose tasks is harder for coding compared to Minecraft. Minecraft is an open world environment, so the space of valid tasks is large. Coding tasks on the other hand are constrained by syntax, execution accuracy for test case etc.

### TODO: Other limitations

- always learning: skill bloat


### TODO: How current work solved some of these limitations
- Omni EPIC
- JARVIS (one?)

## TODO: Conclusion

## TODO: Future Work
- Solve limitations
- LM can’t give tasks – get it to choose from train set instead
- Summarize existing skill level


## References
1. Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L. and Anandkumar, A., 2023. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291.
2. Liu, J., Xia, C.S., Wang, Y. and Zhang, L., 2024. Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation. Advances in Neural Information Processing Systems, 36.
3. Austin, J., Odena, A., Nye, M., Bosma, M., Michalewski, H., Dohan, D., Jiang, E., Cai, C., Terry, M., Le, Q. and Sutton, C., 2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732.
4. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. and Cao, Y., 2022. React: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629.
5. Shi, Q., Tang, M., Narasimhan, K. and Yao, S., 2024. Can Language Models Solve Olympiad Programming?. arXiv preprint arXiv:2404.10952.
6. Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. and Liang, P., 2024. Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12, pp.157-173.
7. Jain, N., Zhang, T., Chiang, W.L., Gonzalez, J.E., Sen, K. and Stoica, I., 2023. Llm-assisted code cleaning for training accurate code generators. arXiv preprint arXiv:2311.14904.

## Appendix
see [APPENDIX](APPENDIX.md)