##########
# import #
##########
import textwrap
from pathlib import Path
from utils import utils


#############
# Blueprint #
#############
class Blueprint:

    ############
    # __init__ #
    ############
    def __init__(self):
        """
        Blueprint constructor.
        """
        pass

    ##########
    # indent #
    ##########
    def indent(self, txt, spaces = 0):
        """
        Indents every line of txt by the given number of spaces.

        Args:
            txt (str): Text to indent.
            spaces (int, optional): Number of spaces to indent. Defaults to 0.

        Returns:
            str: Indented text.
        """
        return textwrap.indent(txt, " " * spaces)

    ########
    # eval #
    ########
    def eval(self, txt, params = None):
        """
        Evaluates a template string and returns the resulting text.

        The template is a Python script that builds a string assigned to the
        variable 'txt'. The 'params' dict and a 'blueprint' reference are
        injected into the template's namespace.

        Args:
            txt (str): Template string to evaluate.
            params (dict, optional): Parameters to pass into the template. Defaults to {}.

        Returns:
            str: The text produced by evaluating the template.
        """
        if params is None:
            params = {}

        namespace = {"blueprint": self, "params": params}

        utils.exec(txt, namespace)

        return namespace["txt"]

    ###########
    # include #
    ###########
    def include(self, filename, params = None, spaces = 0):
        """
        Reads a template file, evaluates it, and returns the resulting text.

        Args:
            filename (str): Path to the template file.
            params (dict, optional): Parameters to pass into the template. Defaults to {}.
            spaces (int, optional): Number of spaces to indent the output. Defaults to 0.

        Returns:
            str: The evaluated and indented text.
        """
        return self.indent(self.eval(utils.read(filename), params), spaces)


blueprint = Blueprint()


if __name__ == '__main__':
    print(blueprint)
