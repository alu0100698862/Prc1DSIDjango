#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworlddjango.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
<<<<<<< HEAD
=======
    
>>>>>>> b7b9ddbfb82ea3d0466fe5e45a026ad93c60f9bb
