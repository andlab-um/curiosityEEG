function EEG = EGI_int_ref_ASR_ICA(root_path, sub, in_file, out_file, ica_components)

% set path
mff_path = fullfile(root_path, in_file); % Task_uncleaned_renamed
set_path = fullfile(root_path, out_file); % Task_set_ICA


% set file name
if sub < 10
    fname = fullfile(mff_path, strcat('tc_00', num2str(sub),'_renamed.set'));
    outname = fullfile(set_path, strcat('tc_00', num2str(sub),'_adj_ICA.set'));
else
    fname = fullfile(mff_path, strcat('tc_0', num2str(sub),'_renamed.set'));
    outname = fullfile(set_path, strcat('tc_0', num2str(sub),'_adj_ICA.set'));
end

rej = readtable('C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\rejChannel.csv'); % file contains info of to-be-rejected channel 
rej = table2cell(rej);
fprintf(['>> rejecting & interpolating & rereferring & correcting & ICA: sub ' num2str(sub) ' <<\n']);

% import data
EEG = pop_loadset({fname});

% reject bad channels
originalEEG = EEG;
EEG = pop_select(EEG, 'nochannel', {rej{sub,:}}); % 

% TODO: remove flat channels except for ref
EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion', 'off', 'ChannelCriterion', 0.8, 'LineNoiseCriterion', 4, 'Highpass', 'off', ...
    'BurstCriterion', 'off', 'WindowCriterion', 'off', 'BurstRejection', 'off', 'Distance', 'Euclidian');

% interpolate channels
EEG = pop_interp(EEG, originalEEG.chanlocs, 'spherical');

% re-reference
EEG = pop_reref(EEG, []);

% correct bad data periods by ASR
EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion', 'off', 'ChannelCriterion', 'off', 'LineNoiseCriterion', 'off', 'Highpass', ...
'off', 'BurstCriterion', 20, 'WindowCriterion', 'off', 'BurstRejection', 'off', 'Distance', 'Euclidian');

% re-reference
EEG = pop_reref(EEG, []);

% ICA
EEG = pop_runica(EEG, 'icatype', 'runica', 'extended', 1, 'interrupt', 'on', 'pca', ica_components);

% save to .set
EEG = pop_saveset(EEG, 'filename', outname, 'filepath', '');

