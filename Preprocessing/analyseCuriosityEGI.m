%% -- Pre-processing pipeline for CuriosityEGI -- %%
clear all; clc;
location_path = 'C:\\Users\\xjl19\\Desktop\\Matlab\\eeglab2021.1\\sample_locs\\GSN129.sfp';
root_path = 'C:\\Users\\xjl19\\Desktop\\CuriosityEGI';
% sub = [7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:46,48:57,59:63];


% %% 1. resample, filter 
% % 这里因为前后原始数据命名方式有点不一样 而且我放在不同文件夹里了 所以分开处理的 没有放在一个循环里
% fprintf(['>> Resample, Filter and Select Channel----\n']);
% EGI_resample_filter_chl(root_path, 'FilteredTask', 'Task_set_raw', 'Task_set_uncleaned', 256, 1, 30);
% 

for sub = [7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:46,48:57,59:63] % see parfor
    %% 2. rename marker %%
%     fprintf(['>> Rename marker ----\n']);
%     rename_marker(root_path, sub, 'Task_set_uncleaned', 'Task_uncleaned_renamed');
% 
% 
%     %% 3. reject, interpolate, rereference, correction, ICA %%
%     fprintf(['>> Interpolate, Rereference, Correction, and ICA ----\n']);
%     EGI_int_ref_ASR_ICA(root_path, sub, 'Task_uncleaned_renamed', 'Task_set_ICA', 80);
%      
%     
%     %% 4. Remove components by ICA %%
%     fprintf(['>> Remove components by ICA ----\n']);
%     EGI_ICArm(root_path, sub, 'Task_set_ICA', 'Task_set_ICArm', 0.9);
%     
%     
    %% 6. Epoch %%
%     fprintf(['>> Epoching by Curiosity ----\n']);
%     epoch_erp(root_path, sub, 'Task_set_ICArm', 'curiosity');
%     
%     fprintf(['>> Epoching by Surprise ----\n']);
%     epoch_erp(root_path, sub, 'Task_set_ICArm', 'surprise');
%     
%     fprintf(['>> Epoching by Condition ----\n']);
%     epoch_erp(root_path, sub, 'Task_set_ICArm', 'condition');
    
    
    %% 7. Export ERP %%
%     avgformula_301 = ['nch1 =(ch4 + ch5 + ch6 + ch11 + ch12 + ch28 + ch29 + ch34 + ch48 + ch49+' ...
%         'ch70 + ch71 + ch77 + ch92 + ch93 + ch99 + ch109 + ch10) / 18 label averagechannel'];
%     avgformula_500 = ['nch1 =(ch4 + ch5 + ch6 + ch11 + ch12 + ch28 + ch29 + ch34 + ch48 + ch49+' ...
%         'ch70 + ch71 + ch77 + ch92 + ch93 + ch99 + ch109 + ch69 + ch76 + ch82 + ch91) / 21 label averagechannel'];
%     avgformula_curiosity = ['nch1 =(ch6 + ch28 + ch29 + ch33 + ch34 + ch37 + ch38 + ch42 + ch46 + ch47+' ...
%         'ch48 + ch49 + ch54 + ch55 + ch109) / 15 label averagechannel'];
%     avgformula_500_surprise = ['nch1 =(ch4 + ch5 + ch6 + ch11 + ch12 + ch28 + ch29 + ch34 + ch48 + ch49+' ...
%         'ch70 + ch71 + ch77 + ch92 + ch93 + ch99 + ch109) / 17 label averagechannel'];
%     avgformula_500_condition = ['nch1 =(ch6 + ch29 + ch48 + ch49 + ch55 + ch56 + ch68 + ch69 + ch70+' ...
%         'ch71 + ch75 + ch76 + ch77 + ch81 + ch82 + ch86 + ch90 + ch91 + ch92 + ch93 + ch109) / 21 label averagechannel'];
    avgformula_C = ['nch1 =(ch6 + ch29 + ch49 + ch71 + ch93 + ch109 + ch28 + ch12 + ch5 + ch99 + ch92) / 11 label averagechannel'];
%     avgformula_PL = ['nch1 =( ch34 + ch38 + ch46 + ch47+ ch48 + ch54 + ch55 + ch42 + ch45 + ch53 + ch60) / 11 label averagechannel'];
%     avgformula_PR = ['nch1 = (ch68 + ch69 + ch70 + ch75 + ch76 + ch77 + ch80 + ch81 + ch82 + ch85 + ch86) / 11 label averagechannel'];
%     avgformula_FL = ['nch1 = (ch11 + ch16 + ch17 + ch18 + ch21 + ch22+ ch25 + ch26 + ch27 + ch31) / 10 label averagechannel'];
%     avgformula_FR = ['nch1 = (ch2 + ch3+ ch4 + ch9 + ch98 + ch103 + ch104 + ch105 + ch107 + ch108) / 10 label averagechannel'];
%     fprintf(['>> Exporting by Curiosity data----\n']);
%     export_erpdata(root_path, sub, 'curiosity', avgformula_FR, avgformula_FR);
    
    fprintf(['>> Exporting by Surprise data----\n']);
    export_erpdata(root_path, sub, 'surprise', avgformula_C, avgformula_C);
    
%     fprintf(['>> Exporting by Condition data----\n']);
%     export_erpdata(root_path, sub, 'condition', avgformula_curiosity, avgformula_500_condition);

end

%     %% 5 Assign Bins %%
%     %  by Curiosity Rating [1~6, 0-interrupted] 
%     fprintf(['>> Assign Bins by Curiosity Rating ----\n']);
%     name_bins(root_path, sub, 'Task_set_ICArm', 'curiosity');
%     
%     %  by Surprise Rating [1~6, 0-interrupted] 
%     fprintf(['>> Assign Bins by Surprise Rating ----\n']);
%     name_bins(root_path, sub, 'Task_set_ICArm', 'surprise');
%     
%     %  by Condition [1-continuous 0-interrupted]
%     fprintf(['>> Assign Bins by Surprise Rating ----\n']);
%     name_bins(root_path, sub, 'Task_set_ICArm', 'condition');



