function EEG = EGI_resample_filter_chl(root_path, mff_file1, mff_file2, set_file, srate, low, high)

set_path = fullfile(root_path, set_file); % Task_set_uncleaned


for sub = [7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:43]

    % set path
    mff_path = fullfile(root_path, mff_file1); % Filtered Task
    
    if sub < 10
        fname = fullfile(mff_path, strcat('tc_00', num2str(sub),'_fil.mff'));
        outname = fullfile(set_path, strcat('tc_00', num2str(sub),'_uncleaned.set'));
    else
        fname = fullfile(mff_path, strcat('tc_0', num2str(sub),'_fil.mff'));
        outname = fullfile(set_path, strcat('tc_0', num2str(sub),'_uncleaned.set'));
    end
    fprintf(['>> resampling & filtering: sub ' num2str(sub) ' <<\n']);
    
    % import data
    EEG = pop_mffimport({fname}, {'code'});
    
    % select channels
    EEG = pop_select(EEG, 'nochannel', {'E1', 'E17', 'E32', 'E38', 'E43', 'E48', 'E63', ...
                        'E68', 'E73', 'E81', 'E88', 'E94', 'E99', 'E119', ...
                        'E120', 'E121', 'E125', 'E126', 'E127', 'E128'});
    % resample
    EEG = pop_resample(EEG, srate);
    
    % filter
    EEG = pop_eegfiltnew(EEG, 'locutoff', low);
    EEG = pop_eegfiltnew(EEG, 'hicutoff', high);
    
    % save to .set
    EEG = pop_saveset(EEG, 'filename', outname, 'filepath', '');
end
    
for sub = [44:46,48:57,59:63]    
    
    % set path
    mff_path = fullfile(root_path, mff_file2); % Task_set_raw
    fname = fullfile(mff_path, strcat('temporal_curiosity_0', num2str(sub),'_hq.mff'));
    outname = fullfile(set_path, strcat('tc_0', num2str(sub),'_uncleaned.set'));

    fprintf(['>> resampling & filtering: sub ' num2str(sub) ' <<\n']);
    
    % import data
    EEG = pop_mffimport({fname}, {'code'});
    
    % select channels
    EEG = pop_select(EEG, 'nochannel', {'E1', 'E17', 'E32', 'E38', 'E43', 'E48', 'E63', ...
                        'E68', 'E73', 'E81', 'E88', 'E94', 'E99', 'E119', ...
                        'E120', 'E121', 'E125', 'E126', 'E127', 'E128'});
    % resample
    EEG = pop_resample(EEG, srate);
    
    % filter
    EEG = pop_eegfiltnew(EEG, 'locutoff', low);
    EEG = pop_eegfiltnew(EEG, 'hicutoff', high);
    
    % save to .set
    EEG = pop_saveset(EEG, 'filename', outname, 'filepath', '');
end


