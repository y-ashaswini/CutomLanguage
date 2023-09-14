import sys

class Errors:
    def __init__(self):
        self.error_found = False
        self.errors = []

    def is_error(self):
        if len(self.errors) != 0:
            self.error_found = True
        return self.error_found

    def print_error(self):
        if self.is_error():
            print("ERRORS")
            for i in self.errors:
                print("Type:", i.error_type)
                print("Location:", i.error_location)
                print("Error Message:", i.error_message)
            print()

    def append_error(self, error_type="MISC", error_message="", error_location="MISC"):
        error = {
            error_type: error_type,
            error_message: error_message,
            error_location: error_location,
        }
        self.errors.append(error)
        if not self.error_found:
            self.error_found = True

    def print_last_error(self):
        if self.is_error():
            err = self.errors[-1]
            print("Type:", err.error_type)
            print("Location:", err.error_location)
            print("Error Message:", err.error_message)

    def kill(self):
        self.print_error()
        sys.exit("Found Errors, Terminating Code")