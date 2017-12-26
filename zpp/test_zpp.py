import unittest
import os
import subprocess


DIR = os.path.dirname(__file__)
TEST_CASES_DIR = os.path.join(DIR, 'test-cases')


class TestZpp(unittest.TestCase):
    """Test case for zpp."""

    def test_identical_binaries(self):
        """Assemble zpp output and compare with known results.

        DESCRIPTION/INTRODUCTION
        ========================

        The most direct way of testing the behavior of zpp is
        to compare its output (assembler source files) with
        known results.  However, this approach will be brittle
        because formatting changes will cause failures.
        Therefore, for now we instead test whether assembling the
        output of zpp produces the same result as assembling 
        the source it is supposed to generate.

        TESTING PROCEDURE
        =================

        <TEST_CASES_DIR>/
            <case 1>/
                actual.zpp
                expected.asm
            <case 2>/
                actual.zpp
                expected.asm
            ...
            <case n>/
                actual.zpp
                expected.asm

        The directory with path TEST_CASES_DIR contains a subdirectory
        corresponding to each test case to be checked, where each
        test case subdirectory contains two files: `actual.zpp` and
        `expected.asm`.  To verify a test case, we use `zpp` to
        generate `actual.asm` from `actual.zpp`, and then use an
        assembler to generate `actual.hex` from `actual.asm`.  We then
        use an assembler to generate `expected.hex` from `expected.asm`
        and compare the HEX files, assessing success if and only if
        the HEX files match exactly.

        """
        for case_dir in os.scandir(TEST_CASES_DIR):
            with self.subTest(case=os.path.basename(case_dir.path)):
                _preprocess_file('actual.zpp', 'actual.asm', case_dir.path)
                _assemble_file('actual.asm', 'actual.hex', case_dir.path)
                _assemble_file('expected.asm', 'expected.hex', case_dir.path)
                self.assertTrue(_check_files_match(
                    'actual.hex', 'expected.hex', case_dir.path))


def _preprocess_file(zpp_filename, asm_filename, base_dir):
    """Run zpp on zpp_filename to produce asm_filename."""
    zppfile = os.path.join(base_dir, zpp_filename)
    asmfile = os.path.join(base_dir, asm_filename)

    _run_process('zpp', '-o', asmfile, zppfile)


def _assemble_file(input_filename, output_filename, base_dir):
    """Assemble input_filename into output_filename."""
    infile = os.path.join(base_dir, input_filename)
    outfile = os.path.join(base_dir, output_filename)

    _run_process('spasm', infile, outfile)


def _check_files_match(left, right, base_dir):
    """Check whether files left and right are identical."""
    with open(os.path.join(base_dir, left), 'r') as left_file:
        with open(os.path.join(base_dir, right), 'r') as right_file:
            result = (left_file.read() == right_file.read())

    return result


def _run_process(*args):
    """Run process specified by args."""
    subprocess.run(args, stdout=subprocess.DEVNULL)
