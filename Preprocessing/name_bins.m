function EEG = name_bins(root_path, sub, set_file, by)

eeglab;
% set path
set_path = fullfile(root_path, set_file); % Task_set_ICArm
out_path = fullfile(root_path, strcat('Task_bins_', by)); % Task_bins_curiosity/suprise/condition

% use EEGLAB GUI to load data set
% in EEGLAB GUI - Datasets - select multiple datasets - select all the
% dataset needed

% read csv file from local disk
% remember to include the full path of the file as the first paramater in
% function readtable()
Curiosity_T = readtable('C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\202109data\\202109data\\curi_behav_continuous_0824.csv');
% Curiosity_T = readtable('curi_behav_continuous_0824.csv');

% for sub = (start, end)
% inclusive for start and end
% set file name
% fname = 'tc_NUM_ICArm.set'
% outname = 'tc_NUM_bins.set'
% SETNUM < 10 : tc_00SETNUM
% SETNUM > 10 : tc_0SETNUM
if sub < 10
    fname = strcat('tc_00', num2str(sub),'_ICArm.set');
    outname = strcat('tc_00', num2str(sub),'_bins_', by,'.set');
else
    fname = strcat('tc_0', num2str(sub),'_ICArm.set');
    outname = strcat('tc_0', num2str(sub),'_bins_', by,'.set');
end  
fprintf(['>> renaming: sub ' num2str(sub) 'by' by ' <<\n']);
% import set
EEG = pop_loadset(fname, set_path);
% EEG = pop_loadset({fname});

% data slice
% fetch all records where Participant.id == 7( you can this number to the
% participant you want)
% store the data slice in a temp table
% reference:
% https://www.mathworks.com/matlabcentral/answers/366254-how-do-i-extract-certain-data-from-a-table
Temp_T = Curiosity_T(Curiosity_T.ParticipantID == sub, :);

% sort the table based on Trials Number
Temp_T = sortrows(Temp_T,'Trials_thisN','ascend');

% build a map object
% map<key, val> : key -> val
% key : Trials Num
% val : Curiosity Response
keySet = Temp_T.Trials_thisN;
switch by
    case 'curiosity'
        valSet = Temp_T.Curiosity_response;
    case 'surprise'
        valSet = Temp_T.Surprise_response;
    case 'condition'
        valSet = Temp_T.condition;
    otherwise
        warning('empty BY parameter')
end

% you can use the following two commands to check the map's keySet and
% valueSet
% keys(M)
% values(M)

% you can access values by key
% if the key is not in map, an error message would print in Command Window
%
% M(101) : 
% here 101 is Trial Number, 
% and the value it returned is the BY of 101
Map = containers.Map(keySet, valSet); 

% rename markers
% rename code 0301
for i = 1:length(EEG.event)
    if isKey(Map, str2double(EEG.event(i).code)) % 起点
        rowTrial = i; 
        row0301 = i;
        % next row which have val as '0301' 
        % is 2 lines below '000X'(trial num)
        while row0301 < length(EEG.event) && convertCharsToStrings(EEG.event(row0301).code) ~= '0301'
            row0301 = row0301 + 1;
            if row0301 == length(EEG.event)
                break;
            end
            if str2double(EEG.event(row0301).code) < 135
                break;
            end
        end
        
        str_response = num2str(Map(str2double(EEG.event(rowTrial).code)));
        if str_response == '1'
            str_response = '9';
        end

        EEG.event(row0301).code = append(str_response, num2str(str2num(EEG.event(row0301).code)));
        EEG.event(row0301).type = append(str_response, num2str(str2num(EEG.event(row0301).type)));
    end
end

% rename code X500
for i = 1:length(EEG.event)
    if isKey(Map, str2double(EEG.event(i).code)) % 起点
        rowTrial = i; 
        row0500 = i;
        % next row which have val as '0500 
        % is 2 lines below '000X'(trial num)
        while convertCharsToStrings(EEG.event(row0500).code) ~= '0500'
            row0500 = row0500 + 1;            
            if row0500 == length(EEG.event)
                break;
            end
        end
        str_response = num2str(Map(str2double(EEG.event(rowTrial).code)));
        EEG.event(row0500).code = append(str_response , num2str(str2num(EEG.event(row0500).code)));
        EEG.event(row0500).type = append(str_response , num2str(str2num(EEG.event(row0500).type)));
    end
end

% save to .set
EEG = pop_saveset(EEG, 'filename', outname, 'filepath', out_path);



