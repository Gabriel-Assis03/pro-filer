from pro_filer.actions.main_actions import show_preview  # NOQA
# import pytest

def test_show_preview_1(capsys):
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    expected = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected

def test_show_preview_2(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }
    expected = (
        "Found 0 files and 0 directories\n"
    )
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected

def test_show_preview_3(capsys):
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py", "src/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    expected = (
        "Found 4 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected

def test_show_preview_4(capsys):
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py", "src/__init__.py", "src/__init__.py", "src/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    expected = (
        "Found 6 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/__init__.py', 'src/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected
