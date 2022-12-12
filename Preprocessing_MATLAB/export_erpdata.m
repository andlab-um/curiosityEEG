function EEG = export_erpdata(root_path, sub, by, avgformula_301, avgformula_500)

% set path
set_path = fullfile(root_path, strcat('Task_bins_', by));
out_path = fullfile(set_path, 'export_eegdata');

data_path_301 = fullfile(set_path, 'SET_301'); 
data_path_500 = fullfile(set_path, 'SET_500');

event_path_301_18E = fullfile(out_path, '301_18E');
event_path_500_21E = fullfile(out_path, '500_21E');


if sub < 10
    fname_301 = strcat('tc_00', num2str(sub),'_301.set');
    fname_500 = strcat('tc_00', num2str(sub),'_500.set');

    outdata_301 = strcat('tc_00', num2str(sub),'_301data.txt');
    outevent_301 = strcat('tc_00', num2str(sub),'_301event.txt'); 

    outdata_500 = strcat('tc_00', num2str(sub),'_500data.txt');
    outevent_500 = strcat('tc_00', num2str(sub),'_500event.txt');
else
    fname_301 = strcat('tc_0', num2str(sub),'_301.set');
    fname_500 = strcat('tc_0', num2str(sub),'_500.set');

    outdata_301 = strcat('tc_0', num2str(sub),'_301data.txt');
    outevent_301 = strcat('tc_0', num2str(sub),'_301event.txt');
    
    outdata_500 = strcat('tc_0', num2str(sub),'_500data.txt');
    outevent_500 = strcat('tc_0', num2str(sub),'_500event.txt');
end

% ------------------- 301 -------------------------------------- 301 -------------------------------------- 301 -------------------
% 18E (17E+10
EEG = pop_loadset('filename', fname_301, 'filepath', data_path_301);
EEG = pop_eegchanoperator(EEG, {avgformula_301} , 'ErrorMsg', 'popup', 'KeepChLoc', 'on', 'Warning', 'on'); 

pop_export(EEG, fullfile(out_path, '301_18E', outdata_301), 'transpose', 'on', 'precision', 3);
pop_expevents(EEG, fullfile(event_path_301_18E, 'event', outevent_301));

% ------------------- 500 -------------------------------------- 500 -------------------------------------- 500 -------------------
% 21E (17E+69 76 82 92
EEG = pop_loadset('filename', fname_500, 'filepath', data_path_500);
EEG = pop_eegchanoperator(EEG, {avgformula_500} , 'ErrorMsg', 'popup', 'KeepChLoc', 'on', 'Warning', 'on'); 

pop_export(EEG, fullfile(out_path, '500_21E', outdata_500), 'transpose', 'on', 'precision', 3);
pop_expevents(EEG, fullfile(event_path_500_21E, 'event', outevent_500));





