## View the webpage version of this markdown file at https://km4htc.github.io/farrowandball/


---
title: "farrowandball"
author: "Alex Styer"
date: "6/16/2021"
output:
  html_document: default
  pdf_document: default
---

# Farrow&Ball
The farrowandball package includes 20 preset color palettes of Farrow&Ball paint colors. Main functions include scale_fill_fb() and scale_color_fb() to be applied to ggplot2 objects; these automatically ramp to provide the number of colors needed and can be set to discrete or continuous. plotpal() is an additional helper function to quickly plot a preset palette to view colors alongside hex codes if you wish to create a new manual palette on the fly.

#### Install
install_github("km4htc/farrowandball")

## The palettes
```{r}
library(ggplot2)
library(farrowandball)
library(patchwork)
```

```{r}
# deepspec
deepspec <- plotpal("deepspec") + ggtitle("deepspec")
# spec
spec <- plotpal("spec") + ggtitle("spec")
# lightspec
lightspec <- plotpal("lightspec") + ggtitle("lightspec")

p <- deepspec | spec | lightspec
p
```

```{r}
x <- letters[1:25]
y <- rep(1, 25)
df <- data.frame(x,y)

# day
day <- ggplot(df, aes(x=x, y=y, fill=x)) +
        geom_bar(stat="identity") +
        scale_fill_fb("day", guide = "none") +
        theme(axis.text = element_blank(),
              axis.title = element_blank(),
              panel.background = element_blank(),
              axis.ticks = element_blank()) +
        ggtitle("day")
  
# daylong
daylong <- ggplot(df, aes(x=x, y=y, fill=x)) +
        geom_bar(stat="identity") +
        scale_fill_fb("daylong", guide = "none") +
        theme(axis.text = element_blank(),
              axis.title = element_blank(),
              panel.background = element_blank(),
              axis.ticks = element_blank()) +
        ggtitle("daylong")

# mono
mono <- ggplot(df, aes(x=x, y=y, fill=x)) +
        geom_bar(stat="identity") +
        scale_fill_fb("mono", guide = "none") +
        theme(axis.text = element_blank(),
              axis.title = element_blank(),
              panel.background = element_blank(),
              axis.ticks = element_blank()) +
        ggtitle("mono")

p <- day / daylong / mono
p
```

```{r}
x <- letters[1:4]
y <- rep(1, 4)
df <- data.frame(x,y)

tonka <- ggplot(df, aes(x=x, y=y, color=x)) +
  geom_point(size = 50) +
  scale_color_fb("tonka", guide = "none") +
  scale_y_continuous(limits = c(1,1), expand = c(0, 0)) +
  theme(axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background = element_blank(),
        axis.ticks = element_blank()) +
        annotate("text", x="a", y= 1, label="tonka", size = 5)

dockers <- ggplot(df, aes(x=x, y=y, color=x)) +
  geom_point(size = 50) +
  scale_color_fb("dockers", guide = "none") +
  scale_y_continuous(limits = c(1,1), expand = c(0, 0)) +
  theme(axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background = element_blank(),
        axis.ticks = element_blank()) +
        annotate("text", x="a", y= 1, label="dockers", size = 5)

bellsprout <- ggplot(df, aes(x=x, y=y, color=x)) +
  geom_point(size = 50) +
  scale_color_fb("bellsprout", guide = "none") +
  scale_y_continuous(limits = c(1,1), expand = c(0, 0)) +
  theme(axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background = element_blank(),
        axis.ticks = element_blank()) +
        annotate("text", x="a", y= 1, label="bellsprout", size = 5)

fruitypebbles <- ggplot(df, aes(x=x, y=y, color=x)) +
  geom_point(size = 50) +
  scale_color_fb("fruitypebbles", guide = "none") +
  scale_y_continuous(limits = c(1,1), expand = c(0, 0)) +
  theme(axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background = element_blank(),
        axis.ticks = element_blank()) +
        annotate("text", x="a", y= 1, label="fruitypebbles", size = 5)

p <- tonka / dockers / bellsprout / fruitypebbles
p
```


# Additional palettes
#### Spectral
deepspec,
spec,
lightspec,
lighterspec

#### Divergent
day,
daylong,
army,
mono

#### Base colors
pinks,
pinks2,
reds,
yellows,
greens,
greens2,
blues,
blues2

#### Other
tonka,
bellsprout,
dockers,
fruitypebbles
