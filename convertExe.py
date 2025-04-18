import subprocess
import os

def convert_exe_to_format(exe_file, output_format, data_file, target_dir='.'):
    # if output_format not in ['pdf', 'img']:
    #     raise ValueError("Invalid format. Choose 'pdf' or 'img'.")

    # Specify the file to add and the target directory
    # data_file = 'path/to/your/datafile.txt'
    # target_dir = '.'
    # if output_format not in ['pdf', 'img']:
    #     raise ValueError("Invalid format. Choose 'pdf' or 'img'.")

    # Specify the file to add and the target directory
    target_dir = '.'

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the credentials file and icon file dynamically
    credentials_file = os.path.join(current_dir, 'credentials.txt')
    icon_file = os.path.join(current_dir, 'pdf.ico')

    # Construct the pyinstaller command with --add-data for both data_file and credentials_file, and --icon
    command = [
        'pyinstaller',
        '--noconsole',
        '--onefile',
        f'--add-data={data_file};{target_dir}',
        f'--add-data={credentials_file};{target_dir}',
        f'--icon={icon_file}',
        exe_file
    ]

    # Execute the command
    subprocess.run(command, shell=True)
    # Rename the output file


