import socket


class Config:
    rtsp_port = 8554
    start_udp_port = 5550
    local_ip = socket.gethostbyname(socket.gethostname())

    # Camera(s) settings.
    #    * The keys of this dictionary will be called "camera hash".
    #    * "path" can be used for the storage.
    #    * "url" must contain at least <protocol>://<host>
    #    * Optional: "storage_command" must contain at least two pairs of parentheses (for URL and output file name).
    #       Overrides the same named command from the "storage" section.
    #       Examples:
    #           ffmpeg -i {url} -c copy {filename}.mkv
    #           mencoder {url} -ovc copy -o {filename}.avi
    #           openRTSP -b 10000000 -i -w 1920 -h 1080 -f 15 {url} > {filename}.avi
    #       Note that these utilities aren't included and must be installed yourself.
    #
    cameras = {
        'cameras/camera-1': {
            'path': 'cam-1',
            'url': 'rtsp://USER:password@XXX.XXX.XXX.XXX:XXX',
            # 'storage_command': 'any *nix command for saving rtsp stream to a file',
        },
    }
    court_id = <ID>

    # Force UDP or TCP protocol globally
    tcp_mode = False

    # Limit connections from the web. Set to 0 for unlimited connections
    web_limit = 2

    # Check UDP traffic from cameras, secs
    watchdog_interval = 30

    # Run this script with root permissions or change this path and set up log rotation yourself
    log_file = '<PATH_TO_LOGS>/python-rtsp-server.log'

    # Attention!
    # All files and subdirectories older than "storage_period_days" in this folder will be deleted!
    storage_path = '<PATH_TO_RECORDS_NO_SLASH_AT_THE_END>'
    storage_period_days = 3
    storage_fragment_secs = 900

    # UDP mode:
    storage_command = 'ffmpeg -i {url} -c copy -v error -t {storage_fragment_secs} {filename}.mp4'
    # TCP mode:
    # storage_command = 'ffmpeg -rtsp_transport tcp -i {url} -c copy -v fatal -t {storage_fragment_secs} {filename}.mkv'
    storage_enable = True

    debug = True
