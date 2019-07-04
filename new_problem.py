import sys
from pathlib import Path

def get_arg(arg):
    args = sys.argv
    if arg in args:
        arg_index = args.index(arg) + 1
        if arg_index > len(args):
            sys.stderr.write(f'Arg required for {arg}\n')
            sys.exit(1)
        else:
            return args[arg_index]
    else:
        return None

def main():
    """
    Usage:
        python new_problem.py [-n problem number] [-t problem title] 
    """
    # get number
    # -n - problem number
    problem_num = get_arg('-n')
    if problem_num is None:
        sys.stderr.write('Problem number required. Exiting\n')
        sys.exit()
    title = get_arg('-t')
    if title is None:
        sys.stderr.write('Problem number required. Exiting\n')
        sys.exit()
    
    title = title.replace(' ', '_')

    name = f'{problem_num}_{title}'
    p = Path(name)
    p.mkdir()
    for t in ['C++', 'Python']:
        pp = p / t
        pp.mkdir()

if __name__ == '__main__':
    main()
