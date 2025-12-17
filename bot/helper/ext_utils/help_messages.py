from ..telegram_helper.bot_commands import BotCommands
from ...core.telegram_manager import TgClient
from ..i18n import t

# Mirror help messages
mirror = t("help.mirror.main")
new_name = t("help.mirror.new_name")
multi_link = t("help.mirror.multi_link")
same_dir = t("help.mirror.same_dir")
thumb = t("help.mirror.thumb")
split_size = t("help.mirror.split_size")
upload = t("help.mirror.upload")
user_download = t("help.mirror.user_download")
rcf = t("help.mirror.rcf")
bulk = t("help.mirror.bulk")
rlone_dl = t("help.mirror.rclone_dl")
extract_zip = t("help.mirror.extract_zip")
join = t("help.mirror.join")
tg_links = t("help.mirror.tg_links")
sample_video = t("help.mirror.sample_video")
screenshot = t("help.mirror.screenshot")
seed = t("help.mirror.seed")
zip_arg = t("help.yt.zip")
qual = t("help.yt.quality")
yt_opt = t("help.yt.options")
convert_media = t("help.mirror.convert_media")
force_start = t("help.mirror.force_start")
gdrive = t("help.clone.gdrive")
rclone_cl = t("help.clone.rclone")
name_sub = t("help.mirror.name_sub")
transmission = t("help.mirror.tg_transmission")
thumbnail_layout = t("help.mirror.thumb_layout")
leech_as = t("help.mirror.leech_as")
ffmpeg_cmds = t("help.mirror.ffmpeg_cmds")

# YT help messages
yt = t("help.yt.main")

# Clone help messages
clone = t("help.clone.main")

# Help dictionaries
YT_HELP_DICT = {
    "main": yt,
    "New-Name": f"{new_name}\nNote: Don't add file extension",
    "Zip": zip_arg,
    "Quality": qual,
    "Options": yt_opt,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "Name-Substitute": name_sub,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
}

MIRROR_HELP_DICT = {
    "main": mirror,
    "New-Name": new_name,
    "DL-Auth": t("help.mirror.dl_auth"),
    "Headers": t("help.mirror.headers"),
    "Extract/Zip": extract_zip,
    "Select-Files": t("help.mirror.select_files"),
    "Torrent-Seed": seed,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Join": join,
    "Rclone-DL": rlone_dl,
    "Tg-Links": tg_links,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "User-Download": user_download,
    "Name-Substitute": name_sub,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
}

CLONE_HELP_DICT = {
    "main": clone,
    "Multi-Link": multi_link,
    "Bulk": bulk,
    "Gdrive": gdrive,
    "Rclone": rclone_cl,
}

RSS_HELP_MESSAGE = t("help.rss")

PASSWORD_ERROR_MESSAGE = t("help.password_error")

user_settings_text = {
    "LEECH_SPLIT_SIZE": t("user_settings.leech_split_size", is_premium=TgClient.IS_PREMIUM_USER),
    "LEECH_DUMP_CHAT": t("user_settings.leech_dump_chat"),
    "LEECH_FILENAME_PREFIX": t("user_settings.leech_filename_prefix"),
    "THUMBNAIL_LAYOUT": t("user_settings.thumbnail_layout"),
    "RCLONE_PATH": t("user_settings.rclone_path"),
    "RCLONE_FLAGS": t("user_settings.rclone_flags"),
    "GDRIVE_ID": t("user_settings.gdrive_id"),
    "INDEX_URL": t("user_settings.index_url"),
    "UPLOAD_PATHS": t("user_settings.upload_paths"),
    "EXCLUDED_EXTENSIONS": t("user_settings.excluded_extensions"),
    "INCLUDED_EXTENSIONS": t("user_settings.included_extensions"),
    "NAME_SUBSTITUTE": t("user_settings.name_substitute"),
    "YT_DLP_OPTIONS": t("user_settings.yt_dlp_options"),
    "FFMPEG_CMDS": t("user_settings.ffmpeg_cmds"),
}

help_string = t(
    "help.main",
    mirror_cmd=f"{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}",
    qb_mirror_cmd=f"{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}",
    jd_mirror_cmd=f"{BotCommands.JdMirrorCommand[0]} or /{BotCommands.JdMirrorCommand[1]}",
    nzb_mirror_cmd=f"{BotCommands.NzbMirrorCommand[0]} or /{BotCommands.NzbMirrorCommand[1]}",
    ytdl_cmd=f"{BotCommands.YtdlCommand[0]} or /{BotCommands.YtdlCommand[1]}",
    leech_cmd=f"{BotCommands.LeechCommand[0]} or /{BotCommands.LeechCommand[1]}",
    qb_leech_cmd=f"{BotCommands.QbLeechCommand[0]} or /{BotCommands.QbLeechCommand[1]}",
    jd_leech_cmd=f"{BotCommands.JdLeechCommand[0]} or /{BotCommands.JdLeechCommand[1]}",
    nzb_leech_cmd=f"{BotCommands.NzbLeechCommand[0]} or /{BotCommands.NzbLeechCommand[1]}",
    ytdl_leech_cmd=f"{BotCommands.YtdlLeechCommand[0]} or /{BotCommands.YtdlLeechCommand[1]}",
    clone_cmd=BotCommands.CloneCommand,
    count_cmd=BotCommands.CountCommand,
    delete_cmd=BotCommands.DeleteCommand,
    user_set_cmd=f"{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]}",
    bot_set_cmd=f"{BotCommands.BotSetCommand[0]} or /{BotCommands.BotSetCommand[1]}",
    select_cmd=BotCommands.SelectCommand,
    cancel_task_cmd=f"{BotCommands.CancelTaskCommand[0]} or /{BotCommands.CancelTaskCommand[1]}",
    force_start_cmd=f"{BotCommands.ForceStartCommand[0]} or /{BotCommands.ForceStartCommand[1]}",
    cancel_all_cmd=BotCommands.CancelAllCommand,
    list_cmd=BotCommands.ListCommand,
    search_cmd=BotCommands.SearchCommand,
    status_cmd=BotCommands.StatusCommand,
    stats_cmd=BotCommands.StatsCommand,
    ping_cmd=BotCommands.PingCommand,
    authorize_cmd=BotCommands.AuthorizeCommand,
    unauthorize_cmd=BotCommands.UnAuthorizeCommand,
    users_cmd=BotCommands.UsersCommand,
    add_sudo_cmd=BotCommands.AddSudoCommand,
    rm_sudo_cmd=BotCommands.RmSudoCommand,
    restart_cmd=BotCommands.RestartCommand,
    log_cmd=BotCommands.LogCommand,
    shell_cmd=BotCommands.ShellCommand,
    aexec_cmd=BotCommands.AExecCommand,
    exec_cmd=BotCommands.ExecCommand,
    clear_locals_cmd=BotCommands.ClearLocalsCommand,
    rss_cmd=BotCommands.RssCommand,
)

# For backwards compatibility with existing code that imports these
COMMAND_USAGE = {
    "mirror": (MIRROR_HELP_DICT["main"], None),
    "yt": (YT_HELP_DICT["main"], None),
    "clone": (CLONE_HELP_DICT["main"], None),
}
