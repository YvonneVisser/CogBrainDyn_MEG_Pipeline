"""
============================================
03. Extract events from the stimulus channel
============================================

The events are extracted from stimulus channel 'STI101'. The events are saved
to the subject's MEG directory.
"""

import os.path as op

import mne
from mne.parallel import parallel_func
import numpy as np

import config


def run_events(subject):
    print("processing subject: %s" % subject)
    
    meg_subject_dir = op.join(config.study_path, subject)
    raw_fnames_in = [op.join(meg_subject_dir, 'timelimit_%s_block01_maxfiltered.fif' % subject)]
    eve_fnames_out = [op.join(meg_subject_dir, '%s-eve.fif' % subject)]

    for raw_fname_in, eve_fname_out in zip(raw_fnames_in, eve_fnames_out):
        events = np.load(op.join(meg_subject_dir, 'events_fixed.npy')) # load previously defined events
        #raw = mne.io.read_raw_fif(raw_fname_in)
        #events = mne.find_events(raw, output = 'onset', shortest_event = 2)

        print("subject: %s - file: %s" % (subject, raw_fname_in))
        mne.viz.plot_events(events)
        mne.write_events(eve_fname_out, events)


parallel, run_func, _ = parallel_func(run_events, n_jobs=config.N_JOBS)
subjects_iterable = [config.subjects] if isinstance(config.subjects, str) else config.subjects
parallel(run_func(subject) for subject in subjects_iterable)
