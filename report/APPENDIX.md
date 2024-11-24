# Appendix

## Invalid / Ambiguous error analysis
These questions appeared in the error analysis (right to wrong and vice versa) 
but we discount them as they can be invalid or ambiguous.

### GPT 4o mini
Wrong to right:
- 437: This question is easy but ReAct somehow got it wrong as it did not listen to the critic which suggested the right answer. Voyager got it right but the skills retrieved do not seem relevant, so it might just be due to the context being put in such a way that the vital information is attended to by the coding agent

Right to wrong:
- Mbpp 170: List slicing question. Voyager actually additionally added a validation for the indices being out of bounds, as its retrieved skills did contain some validation code. However, the task gave an adversarial input where the start index is greater than the end index, so ReAct returned a blank list which is deemed correct but Voyager raised an error. 
- 611: Same as 170 except the adversarial input was column "-1" which sounds out of bounds but does actually return something.
- Mbpp 741: Check if all characters in a string are the same. The agents differ in edge case handling. Voyager return `False` for an empty string, while ReAct returns `True`. The retrieved skills do not seem relevant.


### GPT 4o
Wrong to right:
- 472: Check if a list has consecutive numbers. ReAct handled the edge case of less than 2 elements as `False` (it failed the case where the list has one element) while Voyager, influenced by the retrieved skill `has_unique_chars`, checks if the list has unique elements and the length of the list corresponds to the difference between the max and min of the list, thereby returning `True` for a list with one element. While the skill library did influence the outcome, the correct answer is debatable.
- 611: This question was right to wrong in GPT 4o mini. This time, surprisingly, ReAct kept confusing the `nth` column due to 0 or 1 based indexing, and despite the critic suggesting the correct answer, it still got it wrong. Voyager however got it right on the first try, and despite retrieving the same skill that had validation which caused 4o mini to fail, GPT 4 ignored the validation.
- 109: Rotating binary string. Question did not specify the direction of the rotation and it just so happened that Voyager chose the correct direction.
- 285: Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters. The question can be misinterpreted to "reject those with 4 or more 'b' characters following the 'a'", but it is not the case. ReAct and Voyager interpreted them differently
- 735: Toggle middle bits. ReAct decided to handle edge case and prematurely returned a string instead of an int while Voyager did not make that mistake. Skills retrieved were not relevant.
- 767: ReAct returned a value which used a variable which might not be defined in edge cases. However, there isn't anything in the retrieved skills to suggest that Voyager deliberately saw that edge case (it did not even rely on the variable)
- 92: another edge case handling quirk which is ambiguous

Right to wrong
- 437: This is a repeat of the wrong to right in GPT 4o mini, except the situation is reversed.
- 741: Same as in GPT 4o mini.
- 755: Return second smallest number in a list. If there are duplicates (eg consider `[2, 2]`), we count the duplicate as another number so the answer should be 2. However, the official evaluation and both agents discard duplicates; ReAct returns `None` while Voyager, influenced by its retrieved skill, raises ValueError and gets marked wrong. This question seems invalid


## Challenges during implementation
- Original MBPP dataset has errors, use MBPP Plus

## Design considerations

TODO: Differences w original repo

We separate out reasoning and memory modules to make them more easily understood, especially in the context of cognitive architecture / CoALA.


These steps in the original Voyager repo expect a structured format for outputs, so we use pydantic validation with structured output calling to ensure correct format:
- critic (reasoning, success, critique)
- ask and answer questions step before curriculum
- curriculum (for next task. originally doesnt need structured output but for coding tasks, structured output is needed for various components like test cases, task, setup code etc.)


Validation
- Validation functions for code (see coding agent and curriculum agent)


Namespace: original repo loads all skills, but in coding tasks, naming collisions and overriding of builtins is common, so we only load skills when needed.
