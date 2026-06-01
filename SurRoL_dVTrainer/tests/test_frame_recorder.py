import os
import sys
import pytest

# Ensure Python can find the file in the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from multiple_scenes_console_replay import FrameRecorder

@pytest.fixture
def temp_output_dir(tmp_path):
    """Provides a temporary, isolated directory for this specific test."""
    return str(tmp_path)

def test_initialization_creates_directories(temp_output_dir):
    """
    Test: FrameRecorder creating correct directories
    """
    # Initialize the class with temporary test directory
    recorder = FrameRecorder(output_dir=temp_output_dir)
    
    # Assert: Verify the subdirectories were successfully created
    assert os.path.exists(os.path.join(temp_output_dir, "rgb")), "RGB directory missing"
    assert os.path.exists(os.path.join(temp_output_dir, "depth")), "Depth directory missing"
    assert os.path.exists(os.path.join(temp_output_dir, "seg")), "Seg directory missing"