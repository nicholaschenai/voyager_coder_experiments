from agent_expt_suite.eval_setup import core as c

from voyager_coder.utils.argparsers import get_args
from voyager_coder.config import VOYAGER_CONFIG

from cognitive_base.utils.log import setup_logging_n_base_dirs
from cognitive_base.utils.manager import construct_agent


def main(args):
    setup_logging_n_base_dirs(args)
    c.initialize_directories(args)
    c.initialize_environment(args)
    c.save_args(args)

    actor = construct_agent(args, VOYAGER_CONFIG)

    c.train_agent(args, actor)
    
    c.evaluate_agent(args, actor)

    c.cleanup(args)


if __name__ == "__main__":
    args = get_args()
    # set_debug(True)
    # set_verbose(True)
    main(args)
