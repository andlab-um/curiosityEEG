library(patchwork)

# 301 peak to peak: 
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_301\\301_peak\\n2")
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_301\\301_peak\\p3")
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_500\\500_peak\\n")
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_500\\500_peak\\p")

# txt -> csv
filelist <- list.files(pattern = ".txt")
for (i in 1:length(filelist)){
  input <- filelist[i]
  output <- paste0(gsub("\\.txt$", "", input), ".csv")
  print(paste("Processing the file:", input))
  data = read.delim(input, header = TRUE)
  write.table(data, file=output, sep=",", col.names=TRUE, row.names=FALSE)
}

setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_301\\301_peak\\n2")
peakfile <- list.files()
peakfile <- peakfile %>%
  lapply(read.csv)%>%
  bind_rows

summary(peakfile)
write.csv(peakfile[,-4], "tc_301_n2peak.csv")

setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_301\\301_peak\\p3")
peakfile <- list.files()
peakfile <- peakfile %>%
  lapply(read.csv)%>%
  bind_rows
summary(peakfile)
write.csv(peakfile, "tc_301_p3peak.csv")

setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_500\\500_peak\\n")
peakfile <- list.files()
peakfile <- peakfile %>%
  lapply(read.csv)%>%
  bind_rows

summary(peakfile)
write.csv(peakfile, "tc_500_npeak.csv")

setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\Task_bins_curiosity\\ERP_500\\500_peak\\p")
peakfile <- list.files()
peakfile <- peakfile %>%
  lapply(read.csv)%>%
  bind_rows
summary(peakfile)
write.csv(peakfile, "tc_500_ppeak.csv")

# # excel 整理
# setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI")
# ptp <- read.csv("ptp_301.csv")
# 
# # t.test
# t.ptp <- t.test(ptp$ptp_high, ptp$ptp_low, paired=T, alternative="greater")
# t.ptp
# ggplot(ptp, aes(x = ERPset))+
#   geom_point(aes(y=ptp_low), size=2, col="red")+
#   geom_point(aes(y=ptp_high), size=2, col="blue")

# correlation anaysis
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI")
scale <- read.csv("scale_score_bf.csv")
scale <- filter(scale, ID %in% c(7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:46,48:57,59:63))
summary(scale)
ptp301 <- read.csv("ptp_301.csv")
ptp301 <- ptp301 %>% mutate(ID = c(7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:46,48:57,59:63))
ptp500 <- read.csv("ptp_500.csv")
ptp500 <- ptp500 %>% mutate(ID = c(7:9,11:16,18:23,25,27,28,30:34,36,37,39,40,42:46,48:57,59:63))

# all curiosity
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C.RData")
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_C+PL.RData")

# find peak
peak_301_all <- p3_301 %>%
  group_by(sub, Time) %>%
  summarise(averagechannel = mean(averagechannel)) %>% 
  group_by(Time) %>% 
  summarise(averagechannel = mean(averagechannel))

peak_301_level <- p3_301 %>%
  group_by(sub, Time, curiosity) %>%
  summarise(averagechannel = mean(averagechannel)) %>% 
  group_by(Time, curiosity) %>% 
  summarise(averagechannel = mean(averagechannel))

p3peak_301 <- p3_301 %>%
  filter(Time==277.344) %>%
  # filter(Time==292.969) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3peak_301 = mean(averagechannel), ID = mean(ID))

load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C.RData")
p3mean_301 <- p3_301 %>%
  # filter(Time>=285.156 & Time <= 320.312) %>%
  filter(Time>=289.062 & Time <= 320.312) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3mean_301 = mean(averagechannel), ID = mean(ID))
p3mean_301_high <- p3_301 %>%
  filter(curiosity == "high") %>%
  filter(Time>=289.062 & Time <= 320.312) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3mean_301_high = mean(averagechannel), ID = mean(ID))

load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_C+PL.RData")
n2mean_301 <- p3_301 %>%
  # filter(Time>=285.156 & Time <= 320.312) %>%
  filter(Time>=171.875 & Time <= 207.031) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(n2mean_301 = mean(averagechannel), ID = mean(ID))
n2mean_301_high <- p3_301 %>%
  filter(curiosity == "high") %>%
  filter(Time>=171.875 & Time <= 207.031) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(n2mean_301_high = mean(averagechannel), ID = mean(ID))



peak_500_all <- p3_500 %>%
  group_by(sub, Time) %>%
  summarise(averagechannel = mean(averagechannel)) %>% 
  group_by(Time) %>% 
  summarise(averagechannel = mean(averagechannel))

p3peak_500 <- p3_500 %>%
  filter(Time==199.219) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3peak_500 = mean(averagechannel), ID = mean(ID))

load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_PL+C.RData")
p3mean_500 <- p3_500 %>%
  filter(Time>=261.719 & Time <= 324.219) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3mean_500 = mean(averagechannel), ID = mean(ID))
p3mean_500_high <- p3_500 %>%
  filter(curiosity == "high") %>%
  filter(Time>=261.719 & Time <= 324.219) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p3mean_500_high = mean(averagechannel), ID = mean(ID))
p2mean_500 <- p3_500 %>%
  filter(Time>=167.969 & Time <= 191.406) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p2mean_500 = mean(averagechannel), ID = mean(ID))
p2mean_500_high <- p3_500 %>%
  filter(curiosity == "high") %>%
  filter(Time>=167.969 & Time <= 191.406) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(p2mean_500_high = mean(averagechannel), ID = mean(ID))

# diff curiosity 
load("C:/Users/xjl19/Desktop/CuriosityEGI/Task_bins_curiosity/export_eegdata/301_500curiosity_bymean.RData")

diff_301 <- p3_301 %>%
  group_by(sub, Time, curiosity) %>%
  summarise(averagechannel = mean(averagechannel)) %>% 
  pivot_wider(names_from = curiosity, values_from = averagechannel) %>% 
  mutate(diff = high-low)
p3peak_diff_301 <- diff_301 %>%
  # filter(Time==289.062) %>%
  filter(Time==292.969) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(diff_peak_301 = mean(diff), ID = mean(ID))
p3mean_diff_301 <- diff_301 %>%
  # filter(Time>=285.156 & Time <= 320.312) %>%
  filter(Time>=289.062 & Time <= 312.500) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(diff_mean_301 = mean(diff), ID = mean(ID))


diff_500 <- p3_500 %>%
  group_by(sub, Time, curiosity) %>%
  summarise(averagechannel = mean(averagechannel)) %>% 
  pivot_wider(names_from = curiosity, values_from = averagechannel) %>% 
  mutate(diff = high-low)
p3peak_diff_500 <- diff_500 %>%
  filter(Time==191.406) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(diff_peak_500 = mean(diff), ID = mean(ID))
p3mean_diff_500 <- diff_500 %>%
  # filter(Time>=261.719 & Time <= 351.562) %>%
  filter(Time>=167.969 & Time <= 359.375) %>%
  mutate(ID = sub) %>%
  group_by(sub) %>%
  summarise(diff_mean_500 = mean(diff), ID = mean(ID))
scale <- left_join(scale, p3mean_301[,-1], by = "ID")
scale <- left_join(scale, n2mean_301[,-1], by = "ID")

# scale <- left_join(scale, ptp301[,c(2,3,6:8)], by = "ID")
# scale <- left_join(scale, p3peak_301[,-1], by = "ID")
# # scale <- left_join(scale, p3peak_diff_301[,-1], by = "ID")
# scale <- left_join(scale, p3mean_diff_301[,-1], by = "ID")

scale <- left_join(scale, p3mean_500[,-1], by = "ID")
scale <- left_join(scale, p2mean_500[,-1], by = "ID")

scale <- left_join(scale, p3mean_301_high[,-1], by = "ID")
scale <- left_join(scale, n2mean_301_high[,-1], by = "ID")
scale <- left_join(scale, p3mean_500_high[,-1], by = "ID")
scale <- left_join(scale, p2mean_500_high[,-1], by = "ID")


# scale <- left_join(scale, ptp500[,c(2,3,6:8)], by = "ID")
# scale <- left_join(scale, p3peak_500[,-1], by = "ID")
# # scale <- left_join(scale, p3peak_diff_500[,-1], by = "ID")
# scale <- left_join(scale, p3mean_diff_500[,-1], by = "ID")

# # behavioral ratings
# setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI")
# behav_rating <- read.csv("curi_behav_continuous_0824.csv")
# behav_sub <- behav_rating %>% mutate(ID = ParticipantID) %>% 
#   group_by(ID) %>% 
#   summarise(Curiosity.response = mean(Curiosity.response),
#             Surprise.response = mean(Surprise.response),
#             Confidence.response = mean(Confidence.response))
# scale <- left_join(scale, behav_sub, by = "ID")

library(psych)
library(corrplot)
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
scaleP3.cor <- corr.test(scale[,c(3:18)], method="pearson",adjust="fdr")
# scaleP3.cor <- corr.test(scale[,c(11:18)], method="pearson",adjust="fdr")
scaleP3.r <- scaleP3.cor$r
scaleP3.p <- scaleP3.cor$p
green <- colorRampPalette(c("#4477AA", "#77AADD", "#FFFFFF", "#EE9988", "#BB4444"))
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\NewFigures")
png(filename ='correlation_matrix.png', width=4000,height=4000, units = "px", res=400)
# png(filename ='correlation_matrix_erps.png', width=4000,height=4000, units = "px", res=400)
corPlot(scaleP3.r,numbers=TRUE,colors=TRUE,show.legend=TRUE,pval=scaleP3.p, MAR=8.5,
        diag=FALSE,stars=TRUE,adjust="none",gr=green,xlas=2,main='Correlation Matrix')
dev.off()

# further explore the correlations with LM
m1 <- lm(p2mean_500 ~ n2mean_301, data = scale)
summary(m1)
m2 <- lm(p3mean_301 ~ State.anxiety, data = scale)
summary(m2)
m3 <- lm(p2mean_500_high ~ Trait.curiosity, data = scale)
summary(m3)


# plot the correlations
p1 <- ggplot(scale, aes(x = n2mean_301, y = p2mean_500))+
  geom_point(size = 4, alpha =.25)+
  geom_smooth(method = lm, size = 2, fill="lightblue", alpha=.25)+
  xlab("N170 mean amplitude (blurred phase)")+
  ylab("P190 mean amplitude (clear phase)")+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))

p2 <- ggplot(scale, aes(x = State.anxiety, y = p3mean_301))+
  geom_point(size = 4, alpha =.25)+
  geom_smooth(method = lm, size = 2, col=brewer.pal(9, "Purples")[8], fill=brewer.pal(9, "Purples")[5], alpha=.2)+
  xlab("State anxiety")+
  ylab("P300 mean amplitude (blurred phase)")+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))

p3 <- ggplot(scale, aes(x = Trait.curiosity, y = p2mean_500_high))+
  geom_point(size = 4, alpha =.25)+
  geom_smooth(method = lm, size = 2, col=brewer.pal(9, "RdPu")[7], fill=brewer.pal(9, "RdPu")[5], alpha=.15)+
  xlab("Trait curiosity")+
  ylab("P190 high curiosity mean amplitude (clear phase)")+
  theme_classic()+
  theme(axis.line=element_line(linetype=1,color="black",size=1))+
  theme(axis.ticks=element_line(color="black",size=1,lineend = 12))+
  theme(axis.text = element_text(color = "black", size = rel(1.4)))+
  theme(axis.title = element_text(color = "black", size = 18))+
  theme(legend.title = element_text(color = "black", size = 18))+
  theme(legend.text = element_text(color = "black", size = 16))
p1 | p2 | p3

# Save
setwd("C:\\Users\\xjl19\\Desktop\\CuriosityEGI\\NewFigures")
pdf("regression.pdf", width=5.5, height=6) 
print(p1)
print(p2)
print(p3)
dev.off()


m4 <- lm(p3mean_301 ~ IGD20, data = scale)
summary(m4)

p3 <- ggplot(scale, aes(x = State.anxiety, y = p3mean_301))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, col="orange3", fill="orange2", alpha=.12)+
  xlab("State anxiety")+
  ylab("P300 peak amplitude difference (blurred phase)")+
  theme_classic()

p4 <- ggplot(scale, aes(x = IGD20, y = p3mean_301))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, col="darkorange2", fill="darkorange2", alpha=.1)+
  xlab("IGD20")+
  ylab("P300 peak amplitude difference (blurred phase)")+
  theme_classic()

p3 | p4

m5 <- lm(p3peak_500 ~ Trait.curiosity, data = scale)
summary(m5)
m6 <- lm(p3mean_500 ~ Perceptual.curiosity, data = scale)
summary(m6)

p5 <- ggplot(scale, aes(x = Trait.curiosity, y = p3peak_500))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, col="blue", fill="blue", alpha=.08)+
  xlab("Trait curiosity")+
  ylab("P200 peak amplitude (clear phase)")+
  theme_classic()

p6 <- ggplot(scale, aes(x = Perceptual.curiosity, y = p3mean_500))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, fill="lightblue", alpha=.25)+
  xlab("Perceptual curiosity")+
  ylab("P200 mean amplitude (clear phase)")+
  theme_classic()

p5 | p6

m7 <- lm(high_max_500 ~ Trait.curiosity, data = scale)
summary(m7)
# m8 <- lm(diff_peak_500 ~ State.anxiety, data = scale)
# summary(m8)
# m9 <- lm(diff_peak_500 ~ IGD9, data = scale)
# summary(m9)
m10 <- lm(diff_mean_500 ~ Sensation.seeking, data = scale)
summary(m10)
m11 <- lm(diff_mean_500 ~ Sensation.seeking_s, data = scale)
summary(m11)


p7 <- ggplot(scale, aes(x = Trait.curiosity, y = high_max_500))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, col="blue", fill="blue", alpha=.08)+
  xlab("Trait curiosity")+
  ylab("High curiosity P200 peak amplitude (clear phase)")+
  theme_classic()

p10 <- ggplot(scale, aes(x = Sensation.seeking, y = p3mean_500))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, fill="lightblue", alpha=.25)+
  xlab("Sensation seeking")+
  ylab("P200 mean amplitude difference (clear phase)")+
  theme_classic()

p11 <- ggplot(scale, aes(x = Sensation.seeking_s, y = p3mean_500))+
  geom_point(size = 3, alpha =.3)+
  geom_smooth(method = lm, size = 2, fill="lightblue", alpha=.25)+
  xlab("Sensation seeking_s")+
  ylab("P200 mean amplitude difference (clear phase)")+
  theme_classic()

p7 | p10| p11

(p1 | p2) / (p3 | p4)

p1 | p2 | p3 | p4







