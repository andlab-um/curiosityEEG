function EEG = rename_marker(root_path, sub, set_file, out_file)

% % testing
% location_path = 'C:\\Users\\xjl19\\Desktop\\Matlab\\eeglab2021.1\\sample_locs\\GSN129.sfp';
% root_path = 'C:\\Users\\xjl19\\Desktop\\CuriosityEGI';
% sub = [8]; set_file = 'Task_set_uncleaned'; out_file = 'Task_uncleaned_renamed';

% set path
set_path = fullfile(root_path, set_file); % Task_set_uncleaned
out_path = fullfile(root_path, out_file); % Task_uncleaned_renamed

% read csv file from local disk
% remember to include the full path of the file as the first paramater in function readtable()
Curiosity_T = readtable('C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\202109data\\202109data\\curi_behav_continuous_0824.csv');

if sub < 10
    fname = strcat('tc_00', num2str(sub),'_uncleaned.set');
    outname = strcat('tc_00', num2str(sub),'_renamed.set');
else
    fname = strcat('tc_0', num2str(sub),'_uncleaned.set');
    outname = strcat('tc_0', num2str(sub),'_renamed.set');
end  
fprintf(['>> renaming: sub ' num2str(sub) ' <<\n']);

% import set
EEG = pop_loadset(fname, set_path);

% data slice: fetch all records where Participant.id == (e.g., 7)
% store the data slice in a temp table
Temp_T = Curiosity_T(Curiosity_T.ParticipantID == sub, :);

% sort the table based on Trials Number
Temp_T = sortrows(Temp_T,'Trials_thisN','ascend');

% build hashmap objects - map<key, val> : key -> val
% key : Trials Num
% val : Curiosity Response
keySet = Temp_T.Trials_thisN;
valSet1 = Temp_T.Curiosity_response;
valSet2 = Temp_T.Surprise_response;
valSet3 = Temp_T.condition;

% Use the following commands to check the hashmap's keySet and valueSet
% keys(M)
% values(M)

% Can access values by key
% M(101) : 101 is Trial Number, and the value it returned is the BY of 101
% if the key is not in map, an error message would be printed
Map_curi = containers.Map(keySet, valSet1); 
Map_surp = containers.Map(keySet, valSet2); 
Map_cond = containers.Map(keySet, valSet3); 

datable = EEG.event; % create a new struct for replacing EEG.event
row_index = 1; i = 1; % initiate some parameters

% create new markers
% 0301 by curiosity: 7301~7306
% 0301 by surprise: 8301~8306
% 0301 by condition: 9301,0301
% 0500 by curiosity: 7501~7506
% 0500 by surprise: 8501~8506
% 0500 by condition: 9500,0500
while i <= length(EEG.event)
    if isKey(Map_curi, str2double(EEG.event(i).code)) % trial start
        rowTrial = i; 
        rowEvent = i;
        curi_response = num2str(Map_curi(str2double(EEG.event(rowTrial).code))); % '1~6'
        surp_response = num2str(Map_surp(str2double(EEG.event(rowTrial).code))); % '1~6'
        condition = num2str(9);

        while rowEvent < length(EEG.event) && convertCharsToStrings(EEG.event(rowEvent).code) ~= '0301' 
            datable(row_index) = EEG.event(rowEvent);
            rowEvent = rowEvent + 1;
            row_index = row_index + 1;
        end
        
        % 0301 by condition: 9301,0301
        datable(row_index) = EEG.event(rowEvent);
        datable(row_index).code = append(condition, num2str(str2double(datable(row_index).code)));
        datable(row_index).type = append(condition, num2str(str2double(datable(row_index).type)));
        
        % 0301 by curiosity: 7301~7306
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent for curiosity marker
        curi_marker = strcat('730', curi_response);
        datable(row_index).code = curi_marker; 
        datable(row_index).type = curi_marker; 

        % 0301 by surprise: 8301~8306
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent again for surprise marker
        surp_marker = strcat('830', surp_response);
        datable(row_index).code = surp_marker; 
        datable(row_index).type = surp_marker; 

        % 0301 add trial maker
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent for curiosity marker
        trail_marker = EEG.event(i).code;
        datable(row_index).code = trail_marker; 
        datable(row_index).type = trail_marker; 
        datable(row_index).latency = datable(row_index).latency + 50.00;

        

        rowEvent = rowEvent + 1;
        row_index = row_index + 1;

        while rowEvent < length(EEG.event) && convertCharsToStrings(EEG.event(rowEvent).code) ~= '0500'
            datable(row_index) = EEG.event(rowEvent);
            rowEvent = rowEvent + 1;
            row_index = row_index + 1;
        end

        % 0500 by condition: 9500,0500
        datable(row_index) = EEG.event(rowEvent);
        datable(row_index).code = append(condition, num2str(str2double(datable(row_index).code)));
        datable(row_index).type = append(condition, num2str(str2double(datable(row_index).type)));

        % 0500 by curiosity: 7501~7506
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent for curiosity marker
        curi_marker = strcat('750', curi_response);
        datable(row_index).code = curi_marker; 
        datable(row_index).type = curi_marker; 

        % 0500 by surprise: 8501~8506
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent again for surprise marker
        surp_marker = strcat('850', surp_response);
        datable(row_index).code = surp_marker; 
        datable(row_index).type = surp_marker; 

        % 0500 add trial maker
        row_index = row_index+1;
        datable(row_index) = EEG.event(rowEvent); % copy present rowEvent for curiosity marker
        trail_marker = EEG.event(i).code;
        datable(row_index).code = trail_marker; 
        datable(row_index).type = trail_marker; 
        datable(row_index).latency = datable(row_index).latency + 50.00;


        i = rowEvent + 1;
        row_index = row_index + 1;

    else  
        datable(row_index) = EEG.event(i);
        i = i + 1;
        row_index = row_index + 1;
    end
end

EEG.event = datable;

% save to .set
EEG = pop_saveset(EEG, 'filename', outname, 'filepath', out_path);


