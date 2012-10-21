bind = "unix:/tmp/gunicorn.finisht.sock"
daemon = False                   # Whether work in the background
debug = False                    # Some extra logging
logfile = ".gunicorn.log"        # Name of the log file
loglevel = "info"                # The level at which to log
pidfile = ".gunicorn.pid"        # Path to a PID file
workers = 3                      # Number of workers to initialize
umask = 0                        # Umask to set when daemonizing
user = None                      # Change process owner to user
group = None                     # Change process group to group
proc_name = "gunicorn-finisht"     # Change the process name
tmp_upload_dir = None            # Set path used to store temporary uploads
