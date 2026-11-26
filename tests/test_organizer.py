import unittest
import os
import tempfile
from organizer import handle_collision, organize_files


class TestHandleCollision(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.target = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_hidden_file_with_extension(self):
        filename = ".config.json"
        with open(os.path.join(self.target,filename),"w"):
            pass
        result=handle_collision(filename,self.target)
        self.assertEqual(result,".config_1.json")

    def test_basic_collision(self):
        filename = "report.pdf"
        with open(os.path.join(self.target, filename),"w"):
            pass
        result=handle_collision(filename,self.target)
        self.assertEqual(result,"report_1.pdf")

    def test_multiple_filename_types(self):
        test_cases = [
            ("report.pdf", "report_1.pdf"),
            ("README", "README_1"),
            (".bashrc", ".bashrc_1")
        ]
        for filename, expected in test_cases:
            with self.subTest(filename=filename):
                with open(os.path.join(self.target,filename),"w"):
                    pass
                result=handle_collision(filename,self.target)
                self.assertEqual(result,expected)

    def test_increment_suffix(self):
        filenames = ["report.pdf", "report_1.pdf", "report_2.pdf"]
        for filename in filenames:
            with open(os.path.join(self.target,filename),"w"):
                pass
        result=handle_collision("report.pdf",self.target)
        self.assertEqual(result,"report_3.pdf")


class TestOrganizer(unittest.TestCase):

    def setUp(self):
        self.temp_input = tempfile.TemporaryDirectory()
        self.temp_output = tempfile.TemporaryDirectory()
        self.src = self.temp_input.name
        self.dest = self.temp_output.name

    def tearDown(self):
        self.temp_input.cleanup()
        self.temp_output.cleanup()

    def test_pdf_organization(self):
        filename = "report.pdf"
        with open(os.path.join(self.src, filename), "w"):
            pass
        organize_files(self.src, self.dest)
        expected_path = os.path.join(self.dest, "Docs", filename)
        self.assertTrue(os.path.exists(expected_path))
        self.assertFalse(os.path.exists(os.path.join(self.src, filename)))


    def test_multiple_file_categories(self):
        test_files = {
        "photo.jpg": "Images",
        "song.mp3": "Audios",
        "video.mp4": "Videos",
        "script.py": "Exe",
        "archive.zip": "Archives",
        "notes.txt": "Docs",
        "random.xyz": "Others"
        }
        for filename in test_files:
            with open(os.path.join(self.src, filename), "w"):
                pass
        organize_files(self.src, self.dest)
        for filename, category in test_files.items():
            expected_path = os.path.join(self.dest, category, filename)
            with self.subTest(filename=filename):
                self.assertTrue(os.path.exists(expected_path))


    def test_empty_file(self):
        filename = "empty.pdf"
        open(os.path.join(self.src, filename), "w").close()

        organize_files(self.src, self.dest)

        expected_path = os.path.join(self.dest, "Docs", filename)
        self.assertTrue(os.path.exists(expected_path))
        self.assertEqual(os.path.getsize(expected_path), 0)


    def test_file_without_extension(self):
        filename = "README"
        open(os.path.join(self.src, filename), "w").close()

        organize_files(self.src, self.dest)

        expected_path = os.path.join(self.dest, "Others", filename)
        self.assertTrue(os.path.exists(expected_path))


    def test_multiple_dots_filename(self):
        filename = "my.backup.file.txt"
        open(os.path.join(self.src, filename), "w").close()

        organize_files(self.src, self.dest)

        expected_path = os.path.join(self.dest, "Docs", filename)
        self.assertTrue(os.path.exists(expected_path))

    def test_directory_is_skipped(self):
        folder_name = "MyFolder"
        folder_path = os.path.join(self.src, folder_name)
        os.mkdir(folder_path)

        organize_files(self.src, self.dest)

        self.assertTrue(os.path.isdir(folder_path))
        self.assertFalse(os.path.exists(
            os.path.join(self.dest, "Others", folder_name)
        ))

    def test_hidden_file_organization(self):
        filename = ".bashrc"
        open(os.path.join(self.src, filename), "w").close()

        organize_files(self.src, self.dest)

        expected_path = os.path.join(self.dest, "Linux", filename)
        self.assertTrue(os.path.exists(expected_path))


    def test_duplicate_file_organization(self):
        filename = "report.pdf"

        # Create the source file
        open(os.path.join(self.src, filename), "w").close()

        # Create the destination folder and an existing file
        docs_folder = os.path.join(self.dest, "Docs")
        os.makedirs(docs_folder)
        open(os.path.join(docs_folder, filename), "w").close()

        organize_files(self.src, self.dest)

        expected_path = os.path.join(docs_folder, "report_1.pdf")

        self.assertTrue(os.path.exists(expected_path))
        self.assertFalse(os.path.exists(os.path.join(self.src, filename)))