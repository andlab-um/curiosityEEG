function EEG = EGI_ICArm(root_path, sub, in_file, out_file, threshold)

% set path
% root_path = 'C:\\Users\\xjl19\\Desktop\\CuriosityEGI';
mff_path = fullfile(root_path, in_file); % Task_set_ICA
set_path = fullfile(root_path, out_file); % Task_set_ICArm


% set file name
% fname = fullfile(mff_path, 'task_sample.mff');
% outname = fullfile(set_path, 'task_sample.set');
if sub < 10
    fname = fullfile(mff_path, strcat('tc_00', num2str(sub),'_adj_ICA.set'));
    outname_ICArm = fullfile(set_path, strcat('tc_00', num2str(sub),'_ICArm.set'));
else
    fname = fullfile(mff_path, strcat('tc_0', num2str(sub),'_adj_ICA.set'));
    outname_ICArm = fullfile(set_path, strcat('tc_0', num2str(sub),'_ICArm.set'));
end
fprintf(['>> removing: sub ' num2str(sub) ' <<\n']);

% import data
EEG = pop_loadset({fname});

% remove components by ICLabel
EEG = pop_iclabel(EEG, 'default');
% eye: >0.9, muscle: >0.9
EEG = pop_icflag(EEG, [NaN NaN; threshold 1; threshold 1; threshold 1; threshold 1; threshold 1; NaN NaN]);
EEG = pop_subcomp(EEG);

% save to .set
EEG = pop_saveset(EEG, 'filename', outname_ICArm, 'filepath', '');
