# Python program to arrange the files in a directory based on the file's extension  
# Import the necessary modules  
import os  
import shutil  
  
# Define the source directory containing the files to be organized  
# Taking raw input which won't interpret escape characters  
source_dir = input(r"Enter the source directory path : ").replace('\\', '/')  
  
# Define the destination directory where the organized files will be moved to  
# Taking raw input which won't interpret escape characters  
dest_dir = input(r"Enter the destination directory path : ").replace('\\', '/')  
  

  # Create a dictionary to map file extensions to their respective folders  
extension_map = {  
    '.jpg': 'Images',  
    '.png': 'Images',  
    '.gif': 'Images',  
    '.jpeg': 'Images',  
    '.pdf': 'PDF Files',  
    '.txt': 'Text Files',  
    '.docx': 'Word Document',  
    '.rtf': 'Word Document',  
    '.xlsx': 'Excel Files',  
    '.pptx': 'PowerPoint Persentations',  
    '.ppt': 'PowerPoint Persentations',  
    '.mp3': 'Audio',  
    '.wav': 'Audio',  
    '.mp4': 'Video',  
    '.avi': 'Video',  
    '.exe': 'Executable Files',  
    '.py': 'Python Files',  
    '.cpp': 'C++ Files',  
    '.c': 'C Files',  
    '.java': 'Java Files',  
    '.html': 'HTML Files',  
    '.css': 'CSS Files',  
    '.js': 'Javascript Files',  
    '.zip': 'Zip_Files'  
}  
  
# Create the destination folders if they don't already exist  
for folder_name in set(extension_map.values()):  
    os.makedirs(os.path.join(dest_dir, folder_name), exist_ok=True)  
  
# Loop through each file in the source directory and  
# Move it to the appropriate folder in the destination directory  
for filename in os.listdir(source_dir):  
  
    # Get the file extension in lowercase  
    file_ext = os.path.splitext(filename)[-1].lower()  
  
    # Check if the file extension is in the extension_map dictionary  
    if file_ext in extension_map:  
  
        # Create the full path to the source file  
        src_path = os.path.join(source_dir, filename)  
  
        # Create the full path to the destination file  
        dest_path = os.path.join(dest_dir, extension_map[file_ext], filename)  
  
        # Move the file to the appropriate folder in the destination directory  
        shutil.move(src_path, dest_path)  