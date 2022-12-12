function [EEG, ERP] = epoch_erp(root_path, sub, in_file, by)

% set path
set_path = fullfile(root_path, strcat(in_file));
out_path = fullfile(root_path, strcat('Task_bins_', by));
out_path_301 = fullfile(out_path, strcat('SET_301')); % Task_301_curiosity/suprise/condition
out_path_500 = fullfile(out_path, strcat('SET_500'));


% set file name
% bins.txt (a binlist.txt file would have been created)
bins_301 = fullfile(out_path_301, 'bins_301.txt');
bins_500 = fullfile(out_path_500, 'bins_500.txt');

if sub < 10
    fname = strcat('tc_00', num2str(sub),'_ICArm.set');
    % .set
    outname_301 = fullfile(out_path_301, strcat('tc_00', num2str(sub),'_301.set'));
    outname_500 = fullfile(out_path_500, strcat('tc_00', num2str(sub),'_500.set'));
    % elist.txt
    outname_elist = fullfile(out_path, 'elist', strcat('tc_00', num2str(sub),'_elist.txt'));
    outname_elist_301 = fullfile(out_path_301, 'elist_301', strcat('tc_00', num2str(sub),'_301_elist.txt'));
    outname_elist_500 = fullfile(out_path_500, 'elist_500', strcat('tc_00', num2str(sub),'_500_elist.txt'));
    % erp set name
    erpname_301 = strcat('tc_00', num2str(sub),'_301');
    erpname_500 = strcat('tc_00', num2str(sub),'_500');

else
    fname = strcat('tc_0', num2str(sub),'_ICArm.set');
    % .set
    outname_301 = fullfile(out_path_301, strcat('tc_0', num2str(sub),'_301.set'));
    outname_500 = fullfile(out_path_500, strcat('tc_0', num2str(sub),'_500.set'));
    % elist.txt
    outname_elist = fullfile(out_path, 'elist', strcat('tc_0', num2str(sub),'_elist.txt'));
    outname_elist_301 = fullfile(out_path_301, 'elist_301', strcat('tc_0', num2str(sub),'_301_elist.txt'));
    outname_elist_500 = fullfile(out_path_500, 'elist_500', strcat('tc_0', num2str(sub),'_500_elist.txt'));
    % erp set name
    erpname_301 = strcat('tc_0', num2str(sub),'_301');
    erpname_500 = strcat('tc_0', num2str(sub),'_500');
end  
fprintf(['>> epoching: ' fname 'by' by ' <<\n']); 

% ------------------- 301 -------------------------------------- 301 -------------------------------------- 301 -------------------

% import set
EEG = pop_loadset(fname, set_path);

% create eventlist
EEG  = pop_creabasiceventlist(EEG , 'AlphanumericCleaning', 'on', 'BoundaryNumeric', { -99 }, 'BoundaryString', { 'boundary' }, ...
    'Eventlist', outname_elist); 

% assign bins
EEG  = pop_binlister(EEG , 'BDF', bins_301, 'ExportEL', outname_elist_301, 'ImportEL', outname_elist, ...
    'IndexEL',  1, 'SendEL2', 'Text', 'Voutput', 'EEG' ); 

% import eventlist
EEG = pop_importeegeventlist(EEG, outname_elist_301 , 'ReplaceEventList', 'on' ); 

% extract bin-based epoch
EEG = pop_epochbin( EEG , [-200.0  800.0],  'none');

% baseline correction
EEG = pop_rmbase( EEG, [-199  0]);

% compute average erps
ERP = pop_averager( EEG , 'Criterion', 'all', 'DQ_flag', 1, 'DSindex', 1, 'SEM', 'on' );
ERP = pop_savemyerp(ERP, 'erpname', erpname_301, 'filename', strcat(erpname_301,'.erp'), ...
    'filepath', fullfile(out_path, 'ERP_301'), 'Warning', 'off');


% save to .set
EEG = pop_saveset(EEG, 'filename', outname_301, 'filepath', '');    

% ------------------- 500 -------------------------------------- 500 -------------------------------------- 500 -------------------

% import set
EEG = pop_loadset(fname, set_path);

% create eventlist
EEG  = pop_creabasiceventlist(EEG , 'AlphanumericCleaning', 'on', 'BoundaryNumeric', { -99 }, 'BoundaryString', { 'boundary' }, ...
    'Eventlist', outname_elist); 

% assign bins
EEG  = pop_binlister( EEG , 'BDF', bins_500, 'ExportEL', outname_elist_500, 'ImportEL', outname_elist, ...
    'IndexEL',  1, 'SendEL2', 'Text', 'Voutput', 'EEG' ); 

% import eventlist
EEG = pop_importeegeventlist( EEG, outname_elist_500 , 'ReplaceEventList', 'on' ); 

% extract bin-based epoch
EEG = pop_epochbin( EEG , [-200.0  800.0],  'none');

% baseline correction
EEG = pop_rmbase( EEG, [-199 0]);

% compute average erps
ERP = pop_averager( EEG , 'Criterion', 'all', 'DQ_flag', 1, 'DSindex', 1, 'SEM', 'on' );
ERP = pop_savemyerp(ERP, 'erpname', erpname_500, 'filename', strcat(erpname_500,'.erp'), ...
    'filepath', fullfile(out_path, 'ERP_500'), 'Warning', 'off');

% save to .set
EEG = pop_saveset(EEG, 'filename', outname_500, 'filepath', '');    
end



