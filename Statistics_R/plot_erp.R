library(tidyverse)
library(RColorBrewer)

load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C_mean.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_C+PL.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_C+PL_mean.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PR.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_FL.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_FR.RData")

# 301 curiosity
slope_301 <- slope_301 %>% filter(time > 160 & time < 220)
plist <- slope_301$Pr...t..
plist_adj <- p.adjust(plist,  method ="BH") # FDR
slope_301 <- slope_301 %>% mutate(corrected_sig = plist_adj)

p3_301$curiosity <- factor(p3_301$curiosity, levels=c("low","high"))
subavg_301 <- p3_301 %>% 
  group_by(sub,Time,curiosity) %>% summarise(sub_mean = mean(averagechannel)) %>% 
  group_by(Time,curiosity) %>% summarise(mean = mean(sub_mean), se = sd(sub_mean)/sqrt(47))

p.301curiosity <- subavg_301 %>% 
  # filter(Time > 275 & Time < 332) %>%
  # filter(Time > 160 & Time < 220) %>%
  ggplot(aes(x=Time, y=mean))+
  # by mean
  # annotate("rect", xmin=289.062, xmax=316.406, ymin=-.9, ymax=1.1, alpha=.6, fill="gray")+
  # # annotate("rect", xmin=500, xmax=519.531, ymin=-.9, ymax=1.1, alpha=.6, fill="gray")+
  # # annotate("rect", xmin=679.688, xmax=699.219, ymin=-.9, ymax=1.1, alpha=.6, fill="gray")+
  
  # after MCC
  # annotate("rect", xmin=300.781, xmax=325, ymin=-0.1, ymax=1.7, alpha=.7, fill="gray")+ #p3
  # annotate("rect", xmin=179.688, xmax=203.125, ymin=-1.1, ymax=1, alpha=.6, fill="gray")+ #N2
  # annotate("rect", xmin=289.062, xmax=320.312, ymin=-.4, ymax=1.5, alpha=.7, fill="gray")+ #P3
  annotate("rect", xmin=171.875, xmax=207.031, ymin=-1.1, ymax=1.1, alpha=.7, fill="gray")+ #N2
  # geom_ribbon(aes(ymin=mean-se, ymax=mean+se, fill = curiosity), alpha = 1)+
  stat_summary(aes(color = curiosity), geom="line", size=1.6)+
  scale_color_manual(values=c(brewer.pal(9, "Purples")[5],brewer.pal(9, "Purples")[8]))+
  scale_fill_manual(values=c(brewer.pal(9, "Purples")[2],brewer.pal(9, "Purples")[4]))+
  geom_vline(xintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  geom_hline(yintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  ylab("Amplitude")+theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))+
  theme(legend.position = c(1,0.95), legend.justification = c(1,1))
  # theme(legend.position = c(0.02,0.03), legend.justification = c(0,0))
  # theme(legend.position = c(0.02,1), legend.justification = c(0,1))
p.301curiosity

p.301curiosity_PL <- p.301curiosity
p.301curiosity_C <- p.301curiosity
p.301curiosity_PL_mcc <- p.301curiosity
p.301curiosity_C_mcc <- p.301curiosity

p.301curiosity_PL_mcc
p.301curiosity_C_mcc

# 500 curiosity
slope_500 <- slope_500 %>% filter(time > 160 & time < 330)
plist <- slope_500$Pr...t..
plist_adj <- p.adjust(plist,  method ="BH") # FDR
slope_500 <- slope_500 %>% mutate(corrected_sig = plist_adj)

p3_500$curiosity <- factor(p3_500$curiosity, levels=c("low","high"))
subavg_500 <- p3_500 %>% 
  group_by(sub,Time,curiosity) %>% summarise(sub_mean = mean(averagechannel)) %>% 
  group_by(Time,curiosity) %>% summarise(mean = mean(sub_mean), se = sd(sub_mean)/sqrt(47))
p.500curiosity <- subavg_500 %>% 
  filter(Time > 160 & Time < 330) %>%
  ggplot(aes(x=Time, y=mean))+
  # by mean
  # annotate("rect", xmin=-70.312, xmax=-31.250, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  # annotate("rect", xmin=27.344, xmax=58.594, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  # annotate("rect", xmin=167.969, xmax=199.219, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  # annotate("rect", xmin=257.812, xmax=363.281, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  # annotate("rect", xmin=667.969, xmax=710.938, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  # annotate("rect", xmin=765.625, xmax=789.062, ymin=-1.1, ymax=1.55, alpha=.6, fill="gray")+
  
  # after MCC
  annotate("rect", xmin=164.062, xmax=207.031, ymin=-2, ymax=1.8, alpha=.5, fill="gray")+
  annotate("rect", xmin=257.812, xmax=328.125, ymin=-2, ymax=1.8, alpha=.5, fill="gray")+
  
  # annotate("rect", xmin=167.969, xmax=191.406, ymin=-2, ymax=1.4, alpha=.7, fill="gray")+
  # annotate("rect", xmin=261.719, xmax=324.219, ymin=-2, ymax=1.4, alpha=.7, fill="gray")+
  geom_ribbon(aes(ymin=mean-se, ymax=mean+se, fill = curiosity),alpha=1)+
  stat_summary(aes(color = curiosity),geom="line", size=1.8)+
  scale_color_manual(values=c("#CE75AD", brewer.pal(9, "RdPu")[8]))+
  scale_fill_manual(values=c("thistle1", "#E6B9D9"))+
  # geom_vline(xintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  # geom_hline(yintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  ylab("Amplitude")+theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))+
  theme(legend.position = c(0.5,0.05), legend.justification = c(1,0))
p.500curiosity

p.500curiosity_C <- p.500curiosity
p.500curiosity_C_mcc <- p.500curiosity
p.500curiosity_C_mcc

load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PL.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PL_mean.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_C.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_C_mean.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PR.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_PR_mean.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_FL.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_surprise/export_eegdata/500surprise_FR.RData")

# 500 surprise
slope_500 <- slope_500 %>% filter(time > 330 & time < 750)
plist <- slope_500$Pr...t..
plist_adj <- p.adjust(plist,  method ="BH") # FDR
slope_500 <- slope_500 %>% mutate(corrected_sig = plist_adj)

p3_500$surprise <- factor(p3_500$surprise, levels=c("low","high"))
subavg_500 <- p3_500 %>% 
  group_by(sub,Time,surprise) %>% summarise(sub_mean = mean(averagechannel)) %>% 
  group_by(Time,surprise) %>% summarise(mean = mean(sub_mean), se = sd(sub_mean)/sqrt(47))

p.surprise <- subavg_500 %>% 
  filter(Time > 330 & Time < 750) %>% #PL
  # filter(Time > 140 & Time < 680) %>% #C
  # filter(Time > 290 & Time < 800) %>% #PR
  ggplot(aes(x=Time, y=mean))+
  # #by mean
  # annotate("rect", xmin=-70.312, xmax=-46.875, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # annotate("rect", xmin=164.062, xmax=207.031, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # annotate("rect", xmin=265.625, xmax=441.406, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # annotate("rect", xmin=457.031, xmax=562.5, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # annotate("rect", xmin=589.844, xmax=621.094, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # # annotate("rect", xmin=792.969, xmax=796.875, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  # annotate("rect", xmin=691.406, xmax=773.438, ymin=-2, ymax=1.2, alpha=.7, fill="gray")+
  
  #after MCC 
  annotate("rect", xmin=675.781, xmax=687.500, ymin=-0.2, ymax=2.5, alpha=.5, fill="gray")+ #PL p3 not sig
  annotate("rect", xmin=691.406, xmax=714.844, ymin=-0.2, ymax=2.5, alpha=.5, fill="gray")+
  annotate("rect", xmin=730.469, xmax=746.094, ymin=-0.2, ymax=2.5, alpha=.5, fill="gray")+

  # annotate("rect", xmin=148.438, xmax=226.562, ymin=-2.1, ymax=1.8, alpha=.5, fill="gray")+ #C
  # annotate("rect", xmin=234.375, xmax=242.188, ymin=-2.1, ymax=1.8, alpha=.5, fill="gray")+
  # annotate("rect", xmin=246.094, xmax=437.500, ymin=-2.1, ymax=1.8, alpha=.5, fill="gray")+
  # annotate("rect", xmin=464.844, xmax=667.969, ymin=-2.1, ymax=1.8, alpha=.5, fill="gray")+
  
  # annotate("rect", xmin=324.219, xmax=332.031, ymin=-0.8, ymax=2, alpha=.5, fill="gray")+ #PR
  # annotate("rect", xmin=429.688, xmax=468.750, ymin=-0.8, ymax=2, alpha=.5, fill="gray")+ 
  # annotate("rect", xmin=628.906, xmax=675.781, ymin=-0.8, ymax=2, alpha=.5, fill="gray")+ 
  # annotate("rect", xmin=687.500, xmax=796.875, ymin=-0.8, ymax=2, alpha=.5, fill="gray")+ 
  
  # annotate("rect", xmin=332.031, xmax=363.281, ymin=-.5, ymax=2, alpha=.5, fill="gray")+ # PL
  # annotate("rect", xmin=378.906, xmax=410.156, ymin=-.5, ymax=2, alpha=.5, fill="gray")+
  # annotate("rect", xmin=621.094, xmax=746.094, ymin=-.5, ymax=2, alpha=.5, fill="gray")+
  
  # annotate("rect", xmin=148.438, xmax=226.562, ymin=-2, ymax=1.4, alpha=.5, fill="gray")+ # C
  # annotate("rect", xmin=246.094, xmax=441.406, ymin=-2, ymax=1.4, alpha=.5, fill="gray")+
  # annotate("rect", xmin=464.844, xmax=667.969, ymin=-2, ymax=1.4, alpha=.5, fill="gray")+
  
  # annotate("rect", xmin=292.969, xmax=511.719, ymin=-1.1, ymax=2, alpha=.5, fill="gray")+ # PR
  # annotate("rect", xmin=605.469, xmax=796.875, ymin=-1.1, ymax=2, alpha=.5, fill="gray")+ 
  
  geom_ribbon(aes(ymin=mean-se, ymax=mean+se, fill = surprise), alpha=1)+
  stat_summary(aes(color=surprise), geom="line", size=1.8)+
  scale_color_manual(values=c(brewer.pal(9, "Oranges")[4],brewer.pal(9, "Oranges")[7]))+
  scale_fill_manual(values=c(brewer.pal(9, "Oranges")[2],brewer.pal(9, "Oranges")[3]))+
  # geom_vline(xintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  # geom_hline(yintercept=0, linetype="dotted", size = .8, col = "darkgray")+
  ylab("Amplitude")+theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))
  # theme(legend.position = c(0.02,1), legend.justification = c(0,1))
  # theme(legend.position = c(0.28,0.05), legend.justification = c(0,0))
p.surprise

p.surprise_PL <- p.surprise
p.surprise_C <- p.surprise
p.surprise_PR <- p.surprise
p.surprise_PL_mc <- p.surprise
p.surprise_C_mc <- p.surprise
p.surprise_PR_mc <- p.surprise

p.surprise_PL_mcc 
p.surprise_C_mcc
p.surprise_PR_mcc

# Save
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\NewFigures")
pdf("Rfrontal.pdf", width=12, height=6) # Central.pdf, LParietal.pdf, RParietal.pdf, LFrontal.pdf, Rfrontal.pdf 
print(p.301curiosity)
print(p.500curiosity)
print(p.surprise)
dev.off()

pdf("allERP.pdf", width=7.5, height=4.7) 
print(p.301curiosity_PL)
print(p.301curiosity_C)
print(p.500curiosity_C)
print(p.surprise_PL)
print(p.surprise_C)
print(p.surprise_PR)
dev.off()

pdf("mccERPcuriosity.pdf", width=5, height=4.7) 
print(p.301curiosity_PL_mcc)
print(p.301curiosity_C_mcc)
print(p.500curiosity_C_mcc)
dev.off()

pdf("mccERPsurprise.pdf", width=6, height=4.7) 
print(p.surprise_PL_mcc)
print(p.surprise_C_mcc)
print(p.surprise_PR_mcc)
dev.off()

print(p.301curiosity_PL)
print(p.301curiosity_C)
print(p.500curiosity_C)
print(p.surprise_PL)
print(p.surprise_C)
print(p.surprise_PR)





