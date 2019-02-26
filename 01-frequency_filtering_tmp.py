"""
===========================
01. Filter using MNE-python
===========================

The data are bandpass filtered (1 - 40 Hz) using linear-phase fir filter with
delay compensation. For the lowpass filter the transition bandwidth is
automatically defined. See
`Background information on filtering <http://mne-tools.github.io/dev/auto_tutorials/plot_background_filtering.html>`_
for more. The filtered data are saved to separate files to the subject's'MEG'
directory.
"""  # noqa: E501

import os.path as op

import mne
from mne.parallel import parallel_func

import config
import matplotlib.pyplot as plt

# set to True if you want to plot the raw data
do_plot = True

## when using non-maxfiltered data, set to True
#allow_maxshield=True

subject = config.subjects[0]
print("processing subject: %s" % subject)
# XXX : put the study-specific names in the config file
meg_subject_dir = op.join(config.study_path, subject)
raw_fnames_in = [op.join(meg_subject_dir, 'timelimit_%s_block01.fif' % subject)]
raw_fnames_out = [op.join(meg_subject_dir, 'timelimit_%s_block01.fif' % subject)]

for raw_fname_in, raw_fname_out in zip(raw_fnames_in, raw_fnames_out):
    raw = mne.io.read_raw_fif(raw_fname_in, preload=True, verbose='error', allow_maxshield=True)
    # XXX : to add to config.py
    if config.set_channel_types is not None:
        raw.set_channel_types(config.set_channel_types)
    if config.rename_channels is not None:
        raw.rename_channels(config.rename_channels)

    raw.info['bads'] = config.bads[subject]

    # Band-pass the data channels (MEG and EEG)
    raw.filter(
        config.l_freq, config.h_freq,
        l_trans_bandwidth=config.l_trans_bandwidth,
        h_trans_bandwidth=config.h_trans_bandwidth,
        filter_length='auto', phase='zero', fir_window='hamming',
        fir_design='firwin')
    
    if do_plot:
        figure = raw.plot(n_channels = 50,butterfly=True, group_by='position') 
        figure.show()

   # raw.save(raw_fname_out, overwrite=True)


