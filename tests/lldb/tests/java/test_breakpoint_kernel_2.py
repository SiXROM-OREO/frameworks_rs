'''Module that contains the test TestBreakpointKernel2.'''

from harness.test_base_remote import TestBaseRemote


class TestBreakpointKernel2(TestBaseRemote):
    '''Tests the setting of a breakpoint on a RS kernel.'''

    def get_bundle_target(self):
        '''Return string with name of bundle executable to run.

        Returns:
            A string containing the name of the binary that this test can be run
            with.
        '''
        return 'JavaInfiniteLoop'

    def test_case(self, _):
        '''Run the lldb commands that are being tested.

        Raises:
            TestFail: One of the lldb commands did not provide the expected
                      output.
        '''
        # pylint: disable=line-too-long
        self.try_command('language renderscript kernel breakpoint set simple_kernel',
                         ['Breakpoint(s) created'])

        self.try_command('process continue',
                         ['resuming',
                          'stopped',
                          'stop reason = breakpoint'])

        self.try_command('bt',
                         ['stop reason = breakpoint',
                          'frame #0:',
                          'librs.infiniteloop.so',
                          'simple_kernel'],
                         [r'infiniteloop\.rs:2[78]'])

        self.try_command('breakpoint list',
                         ['simple_kernel',
                          'resolved = 1'])

        self.try_command('process status',
                         ['stopped',
                          '.so`simple_kernel',
                          'stop reason = breakpoint'])