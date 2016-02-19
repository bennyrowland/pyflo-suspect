from distutils.core import setup

setup(
        name='pyflo-suspect',
        version='0.0.1',
        packages=['tests', 'pyflo_suspect'],
        url='https://github.com/bennyrowland/pyflo-suspect.git',
        license='MIT',
        author='ben',
        author_email='bennyrowland@mac.com',
        description='Pyflo wrapper for the SUSPECT MRS processing library',
        entry_points={
            "pyflo": [
                "pyflo.mrs.load.twix = pyflo_suspect.load:TwixComponent",
                "pyflo.mrs.svdchannel = pyflo_suspect.processing:SVDChannelWeights",
                "pyflo.mrs.weightedaverage = pyflo_suspect.processing:WeightedAverage",
                "pyflo.mrs.frequency_correction.water_peak_alignment = pyflo_suspect.processing:WaterPeakAlignment",
                "pyflo.mrs.frequency_correction.frequency_shift = pyflo_suspect.processing:FrequencyShift",
                "pyflo.mrs.plot = pyflo_suspect.processing:TempPlot",
            ]
        },
        install_requires=['pyflo', 'suspect', 'pytest', 'mock']
)
