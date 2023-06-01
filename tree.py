#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/py_trees/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
.. argparse::
   :module: py_trees.demos.selector
   :func: command_line_argument_parser
   :prog: py-trees-demo-selector

.. graphviz:: dot/demo-selector.dot

.. image:: images/selector.gif

"""
##############################################################################
# Imports
##############################################################################

import argparse
import py_trees
import sys
import time
import mybehaviour
import py_trees.console as console
import json2code
##############################################################################
# Classes
##############################################################################


def description():
    content = "Higher priority switching and interruption in the children of a selector.\n"
    content += "\n"
    content += "In this example the higher priority child is setup to fail initially,\n"
    content += "falling back to the continually running second child. On the third\n"
    content += "tick, the first child succeeds and cancels the hitherto running child.\n"
    if py_trees.console.has_colours:
        banner_line = console.green + "*" * 79 + "\n" + console.reset
        s = "\n"
        s += banner_line
        s += console.bold_white + "Selectors".center(79) + "\n" + console.reset
        s += banner_line
        s += "\n"
        s += content
        s += "\n"
        s += banner_line
    else:
        s = content
    return s


def epilog():
    if py_trees.console.has_colours:
        return console.cyan + "And his noodly appendage reached forth to tickle the blessed...\n" + console.reset
    else:
        return None


def command_line_argument_parser():
    parser = argparse.ArgumentParser(description=description(),
                                     epilog=epilog(),
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     )
    parser.add_argument('-r', '--render', action='store_true', help='render dot tree to file')
    return parser




##############################################################################
# Main
##############################################################################

def main():
    """
    Entry point for the demo script.
    """
    args = command_line_argument_parser().parse_args()
    print(description())
    py_trees.logging.level = py_trees.logging.Level.DEBUG


    tree = json2code.mycreate()
    ####################
    # Rendering
    ####################
    if args.render:
        py_trees.display.render_dot_tree(tree)
        sys.exit()

    ####################
    # Execute
    ####################
    tree.setup(timeout=15)
    for i in range(1, 9):
        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            tree.tick_once()
            print("\n")
            print(py_trees.display.unicode_tree(root=tree, show_status=True))
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")

main()