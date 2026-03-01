import os

class Margrethe:
    """
    Logs messages to stdout and saves to txt file.

    Attributes:
        width (int): The width of the progress bar.
        pbar_active (bool): Whether a progress bar is currently active.
        dir (str): Directory path where the log file is stored.
    """

    def __init__(self, log_dir, width=100):
        """
        Initializes the Logger instance.

        Creates the log directory if it does not exist and removes any existing
        'log.txt' file.

        Args:
            log_dir (str): Directory where the log file will be stored.
            width (int, optional): Width of the progress bar. Defaults to 100.
        """
        self.width = width
        self.pbar_active = False
        self.dir = log_dir
        os.makedirs(self.dir, exist_ok=True)
        if os.path.exists(os.path.join(self.dir, "log.txt")):
            os.remove(os.path.join(self.dir, "log.txt"))

    def __call__(self, message):
        """
        Allows the Logger instance to be called like a function to log a message.

        Args:
            message (str): The message to log.
        """
        self.str(message)

    def str(self, message):
        """
        Logs a string.

        Args:
            message (str): The message to log.
        """
        self.pbar_active = False
        with open(os.path.join(self.dir, "log.txt"), "a") as f:
            f.write(message + "\n")
            print(message)

    def pbar(self, progress, total):
        """
        Displays or updates a progress bar in both the console and the log file.

        Args:
            progress (int): Current progress value.
            total (int): Total value representing 100% completion.
        """
        with open(os.path.join(self.dir, "log.txt"), "a") as f:
            if not self.pbar_active:
                self.pbar_active = True
            else:
                self._carriage_return()
                print("\r", end="")

            bar = f"|{'=' * int(self.width * progress / total)}{' ' * (self.width - int(self.width * progress / total))}|"
            f.write(bar)
            print(bar, end="")

            if progress == total:
                self.pbar_active = False
                f.write("\n")
                print("\n", end="")

    def _carriage_return(self):
        """
        Moves the file pointer to the beginning of the last line in the log file.

        This allows overwriting the previous progress bar line in the log file.
        """
        with open(os.path.join(self.dir, "log.txt"), "rb+") as f:
            f.seek(0, 2)
            pos = f.tell() - 1

            while pos > 0:
                f.seek(pos)
                if f.read(1) == b"\n":
                    break
                pos -= 1

            f.truncate(pos + 1 if pos > 0 else 0)
