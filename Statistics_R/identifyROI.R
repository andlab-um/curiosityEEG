library(tidyverse)
library(lme4)
library(lmerTest)
library(bruceR)
library(ggsignif)
# 301-PL 500-C
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C.RData")
PL_301 <- p3_301 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PL")
C_500 <- p3_500 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "C")

# 301-PL 500-C
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_C+PL.RData")
C_301 <- p3_301 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "C")
PL_500 <- p3_500 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PL")

# 301-PR 500-PR
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PR.RData")
PR_301 <- p3_301 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PR")
PR_500 <- p3_500 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PR") 

# 301-FL 500-FL
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_FL.RData")
FL_301 <- p3_301 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FL")
FL_500 <- p3_500 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FL")

# 301-FR 500-FR
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_FR.RData")
FR_301 <- p3_301 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FR")
FR_500 <- p3_500 %>% group_by(sub,Time,curiosity) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,curiosity) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FR")

# surprise-C
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_C.RData")
C_surprise <- p3_500 %>% group_by(sub,Time,surprise) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,surprise) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "C")

# surprise-PL
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PL.RData")
PL_surprise <- p3_500 %>% group_by(sub,Time,surprise) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,surprise) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PL")
# surprise-PR
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PR.RData")
PR_surprise <- p3_500 %>% group_by(sub,Time,surprise) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,surprise) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "PR")

# surprise-FL
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_FL.RData")
FL_surprise <- p3_500 %>% group_by(sub,Time,surprise) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,surprise) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FL")

# surprise-FR
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_FR.RData")
FR_surprise <- p3_500 %>% group_by(sub,Time,surprise) %>% 
  summarise(sub_mean = mean(averagechannel)) %>% 
  filter(Time > 275 & Time < 325) %>% 
  group_by(sub,surprise) %>%
  summarise(sub_mean = mean(sub_mean)) %>% mutate(ROI = "FR")

curiosity_blurred <- bind_rows(C_301, PL_301, PR_301, FL_301, FR_301)
curiosity_clear <- bind_rows(C_500, PL_500, PR_500, FL_500, FR_500)
surprise_clear <- bind_rows(C_surprise, PL_surprise, PR_surprise, FL_surprise, FR_surprise)
curiosity_blurred$ROI <- factor(curiosity_blurred$ROI, levels=c("FL","FR","C","PL","PR"))
curiosity_clear$ROI <- factor(curiosity_clear$ROI, levels=c("FL","FR","C","PL","PR"))
surprise_clear$ROI <- factor(surprise_clear$ROI, levels=c("FL","FR","C","PL","PR"))


MANOVA(data=curiosity_blurred, subID='sub', dv='sub_mean', within=c('curiosity','ROI'),sph.correction="GG")
MANOVA(data=curiosity_clear, subID='sub', dv='sub_mean', within=c('curiosity','ROI'),sph.correction="GG")
MANOVA(data=surprise_clear, subID='sub', dv='sub_mean', within=c('curiosity','ROI'),sph.correction="GG")

# m.PL_301 <- lm(sub_mean ~ curiosity, data = PL_301)
# summary(m.PL_301)

t.test(sub_mean ~ curiosity, data = PL_301, paired = T, alternative = "less") # p = 0.032
t.test(sub_mean ~ curiosity, data = PR_301, paired = T, alternative = "greater")
t.test(sub_mean ~ curiosity, data = C_301, paired = T, alternative = "greater") # p = 0.053
t.test(sub_mean ~ curiosity, data = FL_301, paired = T, alternative = "greater")
t.test(sub_mean ~ curiosity, data = FR_301, paired = T, alternative = "less")

t.test(sub_mean ~ curiosity, data = PL_500, paired = T, alternative = "less")
t.test(sub_mean ~ curiosity, data = PR_500, paired = T, alternative = "less")
t.test(sub_mean ~ curiosity, data = C_500, paired = T, alternative = "greater") # p = 0.005
t.test(sub_mean ~ curiosity, data = FL_500, paired = T, alternative = "less")
t.test(sub_mean ~ curiosity, data = FR_500, paired = T, alternative = "less")

t.test(sub_mean ~ surprise, data = PL_surprise, paired = T, alternative = "less") # p = 0.039
t.test(sub_mean ~ surprise, data = PR_surprise, paired = T, alternative = "less") # p = 0.010
t.test(sub_mean ~ surprise, data = C_surprise, paired = T, alternative = "less") # p = 0.000
t.test(sub_mean ~ surprise, data = FL_surprise, paired = T, alternative = "greater")
t.test(sub_mean ~ surprise, data = FR_surprise, paired = T, alternative = "less")


anova.test <- MANOVA(data=curiosity_blurred, subID='sub', dv='sub_mean', within=c('curiosity','ROI'),sph.correction="GG")

t.curiosity_blurred <- curiosity_blurred %>% group_by(curiosity, ROI) %>% 
  summarize(
    mean = mean(sub_mean),
    se = sd(sub_mean)/sqrt(47),
  ) %>% 
  ggplot(aes(ROI, mean, fill = curiosity))+
  geom_bar(position = "dodge", stat="identity")+
  geom_hline(yintercept=0, linetype="dashed", col = "black", size = .7)+
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se),  # add error bar
                width=0.15, color='black', position = position_dodge(.9), size=1)+
  geom_signif(y_position=1.3, xmin=c(2.78), xmax=c(3.23),  # Set the significance note, y_position is the position of the error line on the y-axis, xmin and xmax are the position of the error line on the x-axis, multiple values can be passed in
              annotation=c("*"), tip_length=0.05, size=1, textsize = 10,  # Significance marker; prolongation under significance brackets; size setting; font size
              vjust = 0.3)+  # Adjust the distance between the saliency mark and the saliency brackets
  geom_signif(y_position=1.8, xmin=c(3.78), xmax=c(4.23), 
              annotation=c("*"), tip_length=0.05, size=1, textsize = 10,  vjust = 0.3)+ 
  scale_fill_manual(values=c(brewer.pal(9, "Purples")[8],brewer.pal(9, "Purples")[5]))+
  ylab("P300 Amplitude (high-low)")+ylim(-1.7,1.82)+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))+
  theme(legend.position = c(1,0.05), legend.justification = c(1,0))
t.curiosity_blurred

curiosity_clear$curiosity <- factor(curiosity_clear$curiosity, levels=c("high","low"))
t.curiosity_clear <- curiosity_clear %>% group_by(curiosity, ROI) %>% 
  summarize(
    mean = mean(sub_mean),
    se = sd(sub_mean)/sqrt(47),
  ) %>% 
  ggplot(aes(ROI, mean, fill = curiosity))+
  geom_bar(position = "dodge", stat="identity")+
  geom_hline(yintercept=0, linetype="dashed", col = "black", size = .7)+
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se), width=0.15, color='black', position = position_dodge(.9), size=1)+
  geom_signif(y_position=1.3, xmin=c(2.78), xmax=c(3.23), annotation=c("*"), tip_length=0.05, size=1, textsize = 10, vjust = 0.3)+  
  ylab("P300 Amplitude (high-low)")+ylim(-1.7,1.82)+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))+
  theme(legend.position = c(1,0.05), legend.justification = c(1,0))
t.curiosity_clear

t.surprise_clear <- surprise_clear %>% group_by(surprise, ROI) %>% 
  summarize(
    mean = mean(sub_mean),
    se = sd(sub_mean)/sqrt(47),
  ) %>% 
  ggplot(aes(ROI, mean, fill = surprise))+
  geom_bar(position = "dodge", stat="identity")+
  geom_hline(yintercept=0, linetype="dashed", col = "black", size = .7)+
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se),  # add error bar
                width=0.15, color='black', position = position_dodge(.9), size=1)+
  geom_signif(y_position=1.3, xmin=c(2.78), xmax=c(3.23),  # Set the significance note, y_position is the position of the error line on the y-axis, xmin and xmax are the position of the error line on the x-axis, multiple values can be passed in
              annotation=c("*"), tip_length=0.05, size=1, textsize = 10,  # Significance marker; prolongation under significance brackets; size setting; font size
              vjust = 0.3)+  # Adjust the distance between the saliency mark and the saliency brackets
  geom_signif(y_position=1.7, xmin=c(3.78), xmax=c(4.23), 
              annotation=c("*"), tip_length=0.05, size=1, textsize = 10,  vjust = 0.3)+ 
  geom_signif(y_position=1.8, xmin=c(4.78), xmax=c(5.23), 
              annotation=c("*"), tip_length=0.05, size=1, textsize = 10,  vjust = 0.3)+ 
  scale_fill_manual(values=c(brewer.pal(9, "Oranges")[7],brewer.pal(9, "Oranges")[4]))+
  ylab("P300 Amplitude (high-low)")+ylim(-1.7,1.82)+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))+
  theme(legend.position = c(1,0.05), legend.justification = c(1,0))
t.surprise_clear

# Save
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\NewFigures")
pdf("ttest_ROI.pdf", width=6, height=6) 
print(t.curiosity_blurred)
print(t.curiosity_clear)
print(t.surprise_clear)
dev.off()