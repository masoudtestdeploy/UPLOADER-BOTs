class Translation(object):
    START_TEXT = """سلام {},
من آپلودر کنزوموویم 
میتونی باهام از همه جا دانلود کنی حتی تورنت !!

/help برای دریافت راهنما!"""
    FORMAT_SELECTION = "فرمت مورد نظرت رو انتخاب کن : <a href='{}'>سایز فایل ها تقریبی است</a> \nاگر تامبنیل میخوای یه عکس برام بفرست\nمیتونی از  /delthumbnail برای حذفش استفاده کنی"
    SET_CUSTOM_USERNAME_PASSWORD = """اگر ویدیو پرمیوم میخوای از فرمت زیر استفاده کن:
URL | filename | username | password"""
    DOWNLOAD_START = "📥 در حال دانلود ..."
    UPLOAD_START = "📤 در حال آپلود..."
    RCHD_TG_API_LIMIT = "دانلود در {} ثانیه.\nاندازه فایل شناسایی شده: {}\nشرمندم من نمیتونم فایلای بزرگ تر از 2 گیگ رو آپلود کنم ."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "مرسی که با من بودی\n\n<b>Join : @KenzoMovie</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "دانلود در {} ثانیه.\nآپلود در {} ثانیه.\n\n@KenzoMovie"
    SAVED_CUSTOM_THUMB_NAIL = "عکس شما برای استفاده در تامبنیل ذخیره شد ."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ تامبنیل با موفقیت حذف شد ."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ارور ...\n<b>YouTubeDL</b> خطا : {}"
    HELP_USER = """آموزش استفاده از من خیلی سادست !
    
1. روش ارسال لینک (example.domain/File.mp4 | New Filename.mp4).
(برای دانلود از تورنت فقط magnet بفرست)
2. ارسال عککس برای تامبنیل.
3. انتخاب نوع فایل دریافتی
   Video  - دریافت به صورت ویدیو 
   File   - دریافت به صورت فایل

@KenzoMovie"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "آپلود  {} فایل در {} ثانیه"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    ERROR_YTDLP = "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."
