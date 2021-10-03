import os
import time
from datetime import datetime
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


DOWNLOADS_FOLDER = f"{Path.home()}/Downloads"
PICTURES_FOLDER = f"{Path.home()}/Pictures"
BOOKS_FOLDER = f"{Path.home()}/Ebooks"


def main():
	print(f"Starting the script. Watching folder {DOWNLOADS_FOLDER}")
	print(f"Moving images to {PICTURES_FOLDER}")
	print(f"Moving ebooks to {BOOKS_FOLDER}")
	handler = create_handler()
	create_observer(handler)


def create_observer(handler):
	path = DOWNLOADS_FOLDER
	go_recursively = True
	observer = Observer()
	observer.schedule(handler, path, recursive=go_recursively)

	observer.start()
	try:
		while True:
			time.sleep(5)
	except:
		observer.stop()
	observer.join()


def create_handler():
	patterns = ["*"]
	ignore_patterns = None
	ignore_directories = False
	case_sensitive = True
	handler = PatternMatchingEventHandler(
		patterns, 
		ignore_patterns, 
		ignore_directories, 
		case_sensitive
	)

	handler.on_created = on_created
	handler.on_deleted = on_deleted
	handler.on_modified = on_modified

	return handler


def on_created(event):
	print(f"Created {event.src_path}!")

	if event.is_directory:
		return
	
	extension = get_file_extension(event.src_path)
	folder = None
	if is_img_file(extension) == True:
		folder = PICTURES_FOLDER
	if is_ebook_file(extension) == True:
		folder = BOOKS_FOLDER

	if folder == None:
		return

	if os.path.isdir(PICTURES_FOLDER) == False:
		create_folder(PICTURES_FOLDER)
	
	shutil.move(event.src_path, f"{folder}/{create_file_name(extension)}")


def on_deleted(event):
	print(f"Deleted {event.src_path}!")


def on_modified(event):
	print(f"Modified {event.src_path}!")


def create_folder(path):
	os.mkdir(path, mode = 0o777)


def get_file_extension(path):
	file = path.split("/")[-1]
	return file.split(".")[-1]


def create_file_name(extension):
	name = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
	return f"{name}.{extension}"


def contains(needle, haystack):
	if needle in haystack:
		return True
	else:
		return False


def is_img_file(extension):
	imgs = ["png", "jpg", "jpeg", "gif", "bmp"]
	return contains(extension, imgs)


def is_ebook_file(extension):
	ebooks = ["epub", "pdf", "mob", "azw", "azw3"]
	return contains(extension, ebooks)


if __name__ == "__main__":
	main()