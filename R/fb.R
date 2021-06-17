# Created by Alex Styer at UC Berkeley
# Please share widely!
# All colors come from the Farrow&Ball paint collection

# list of all Farrow&Ball colors used in palettes
fb_colors <- list(
  'Middleton Pink'       = "#fde7e5",
  'Calluna'              = "#ccc8ce",
  'Sugaroom Red'         = "#d0bfcd",
  'Brassica'             = "#8d8089",
  'Pelt'                 = "#50414c",
  'Brinjal'              = "#5e3a42",
  'Preference Red'       = "#6d4247",
  'Sulking Room Pink'    = "#a0837f",
  'Cinder Rose'          = "#c6a4a6",
  'Nancys Blushes'       = "#ecb7b8",
  'Rangwali'             = "#bf7a8f",
  'Lake Red'             = "#c8526a",
  'Rectory Red'          = "#a53c49",
  'Incarnadine'          = "#a04344",
  'Blazer'               = "#b64f48",
  'Harissa'              = "#ae5043",
  'Charlottes Locks'     = "#d65f3d",
  'Book Room'            = "#ab6758",
  'Red Earth'            = "#c57b67",
  'India Yellow'         = "#cb9e59",
  'Sudbury Yellow'       = "#dcb771",
  'Babouche'             = "#ecc363",
  'Yellowcake'           = "#ebe05e",
  'Yellow Ground'        = "#f2cf86",
  'Dayroom Yellow'       = "#f7e29d",
  'Dorset Cream'         = "#efd5a1",
  'Tallow'               = "#fdedd7",
  'Farrows Cream'        = "#efdbb3",
  'Hay'                  = "#dec795",
  'Citrona'              = "#dbcc7c",
  'Churlish Green'       = "#c8bd83",
  'Yeabridge Green'      = "#909e6e",
  'Bancha'               = "#686a47",
  'Duck Green'           = "#465741",
  'Green Ground'         = "#dbdab6",
  'Cooking Apple Green'  = "#c4c6a5",
  'Lichen'               = "#a1a189",
  'Breakfast Room Green' = "#94a68a",
  'Calke Green'          = "#758769",
  'Emerald Green'        = "#7bae72",
  'Verdigris'            = "#3e8b67",
  'Vardo'                = "#427e83",
  'Arsenic'              = "#84b59c",
  'Green Smoke'          = "#737c70",
  'Oval Room Blue'       = "#8b9d9b",
  'Green Blue'           = "#acbdb2",
  'Dix Blue'             = "#99b0ab",
  'Parma Gray'           = "#b1bfc5",
  'Blue Ground'          = "#a1c5c8",
  'Stone Blue'           = "#7997a1",
  'Inchyra Blue'         = "#586768",
  'Hague Blue'           = "#3d4e57",
  'Stiffkey Blue'        = "#4d5b6a",
  'St Giles Blue'        = "#599ec4",
  'Ultra Marine Blue'    = "#5d82a1",
  'Cooks Blue'           = "#6a90b4",
  'Lulworth Blue'        = "#a0b8c8",
  'Pitch Blue'           = "#636e8f",
  'Imperial Purple'      = "#55566b",
  'Scotch Blue'          = "#41404c",
  'Paean Black'          = "#494248",
  'Railings'             = "#45494b",
  'Off Black'            = "#444546",
  'Pitch Black'          = "#3b3938",
  'Pigeon'               = "#a0a093",
  'Old White'            = "#cec3ad",
  'Strong White'         = "#e5e0db",
  'Cabbage White'        = "#e8eeea"
)

# USED INTERNALLY ONLY
# function to return corresponding hex codes for given color name
fb_cols <- function(...) {
  cols <- c(...)
  if (is.null(cols))
    return (fb_colors)
  fb_colors[cols]
}

# USED INTERNALLY ONLY
# generate a list of palettes
# each palette is a list of the required hex codes
fb_pals <- list(
  `all` = fb_colors,

  `pinks`  = fb_cols("Middleton Pink", "Nancys Blushes", "Rangwali",
                       "Lake Red", "Rectory Red"),

  `pinks2`  = fb_cols("Middleton Pink", "Nancys Blushes",
                      "Rangwali", "Brinjal",
                      "Pelt", "Sugaroom Red"),

  `reds`   = fb_cols("Red Earth", "Charlottes Locks", "Blazer",
                       "Rectory Red", "Preference Red"),

  `yellows` = fb_cols("Tallow", "Dayroom Yellow", "Yellow Ground",
                        "Babouche", "India Yellow"),

  `greens`  = fb_cols("Churlish Green", "Yeabridge Green",
                        "Bancha", "Duck Green"),

  `greens2` = fb_cols("Cooking Apple Green", "Breakfast Room Green",
                        "Calke Green", "Duck Green",
                        "Green Smoke", "Railings"),

  `blues` = fb_cols("Parma Gray", "Blue Ground", "Stone Blue",
                      "Inchyra Blue", "Hague Blue"),

  `blues2` = fb_cols("Cabbage White", "Lulworth Blue", "Ultra Marine Blue",
                       "Stiffkey Blue", "Scotch Blue"),

  `deepspec` = fb_cols("Stiffkey Blue", "Hague Blue",
                         "Duck Green", "Bancha",
                         "India Yellow", "Harissa",
                         "Incarnadine", "Brinjal",
                         "Pelt", "Brassica"),

  `spec` = fb_cols("St Giles Blue", "Ultra Marine Blue",
                     "Vardo", "Verdigris", "Emerald Green",
                     "Babouche", "Charlottes Locks",
                     "Rectory Red", "Lake Red", "Rangwali"),

  `lightspec` = fb_cols("Lulworth Blue", "Blue Ground", "Dix Blue",
                          "Breakfast Room Green", "Yeabridge Green",
                          "Dayroom Yellow", "Book Room",
                          "Cinder Rose", "Nancys Blushes"),

  `lighterspec` = fb_cols("Cabbage White", "Parma Gray",
                            "Green Blue", "Cooking Apple Green",
                            "Churlish Green", "Yellow Ground",
                            "Red Earth", "Sugaroom Red",
                            "Middleton Pink"),

  `mono` = fb_cols("Strong White", "Pitch Black"),

  `tonka` = fb_cols("Babouche", "Inchyra Blue",
                      "Blazer", "Off Black"),

  `bellsprout` = fb_cols("Arsenic", "Citrona",
                           "Sulking Room Pink", "Preference Red"),

  `dockers` = fb_cols("Stone Blue", "Calke Green",
                        "Sudbury Yellow", "Scotch Blue"),

  `fruitypebbles` = fb_cols("Lake Red", "Vardo",
                              "Verdigris", "Yellowcake"),

  `day` = fb_cols("Hay", "Farrows Cream", "Green Ground",
                    "Oval Room Blue", "Imperial Purple",
                    "Pitch Blue", "Cooks Blue"),

  `daylong` = fb_cols("Tallow", "Dorset Cream", "Lichen",
                        "Green Smoke", "Inchyra Blue",
                        "Railings", "Pitch Black"),

  `army` = fb_cols("Calluna", "Old White", "Lichen",
                     "Pigeon", "Off Black", "Paean Black")
)

# USED INTERNALLY ONLY
# create a function that allows you to:
# 1) reverse the palette order
# 2) color ramp the palette to expanded it as needed
fb <- function(palette = "spec", reverse = FALSE, ...) {
  pal <- fb_pals[[palette]]
  if (reverse) pal <- rev(pal)
  colorRampPalette(pal, ...)
}


#' scale_color_fb
#' returns a discrete or continuous palette for ggplot2 color. Palettes include: spec, deepspec, lightspec, lighterspec, pinks, pinks2, reds, yellows, greens, greens2, blues, blues2, mono, tonka, bellsprout, dockers, fruitypebbles, day, daylong, and army. Default palette is "deepspec".
#' @param palette name of palette to be used in string format
#' @param discrete set to TRUE if discrete scale desired; FALSE for continuous
#' @param reverse default is FALSE; set to TRUE to reverse the order of the palette
#' @param ...
#'
#' @return returns a ggplot2-compatible color scale based on the template palette given
#' @export
#'
#' @examples
#' scale_color_fb(palette = "daylong", discrete = TRUE, reverse = FALSE)
scale_color_fb <- function(palette = "deepspec", discrete = TRUE, reverse = FALSE, ...) {
  pal <- fb(palette = palette, reverse = reverse)
  if (discrete) {
    ggplot2::discrete_scale("color", paste0("fb ",palette," palette"), palette = pal, ...)
  } else {
    ggplot2::scale_color_gradientn(colours = pal(256), ...)
  }
}


#' scale_fill_fb
#' returns a discrete or continuous palette for ggplot2 fill. Palettes include spec, deepspec, lightspec, lighterspec, pinks, pinks2, reds, yellows, greens, greens2, blues, blues2, mono, tonka, bellsprout, dockers, fruitypebbles, day, daylong, and army. Default palette is "deepspec".
#' @param palette name of palette to be used in string format
#' @param discrete set to TRUE if discrete scale desired; FALSE for continuous
#' @param reverse default is FALSE; set to TRUE to reverse the order of the palette
#' @param ...
#'
#' @return returns a ggplot2-compatible fill scale based on the template palette given
#' @export
#'
#' @examples
#' scale_fill_fb(palette = "deepspec", discrete = TRUE, reverse = FALSE)
#'
#' # See how the palette ramps for the required number of colors
#' # the original "deepspec" palette
#' x <-  letters[1:10]
#' y <-  rep(1, 10)
#' df <- data.frame(x, y)
#' ggplot(df, aes(x=x, y=y, fill=x)) +
#'     geom_bar(stat="identity") +
#'     scale_fill_fb(palette = "deepspec", guide = "none") +
#'     theme(axis.title = element_blank(),
#'           axis.text = element_blank(),
#'           axis.ticks = element_blank(),
#'           panel.background = element_blank())
#'
#' # now deepspec with twice the original colors
#' x <- letters[1:20]
#' y <- rep(1, 20)
#' df <- data.frame(x, y)
#' ggplot(df, (aes(x=x, y=y, fill=x))) +
#'     geom_bar(stat="identity") +
#'     scale_fill_fb(palette = "deepspec", guide = "none") +
#'     theme(axis.title = element_blank(),
#'           axis.text = element_blank(),
#'           axis.ticks = element_blank(),
#'           panel.background = element_blank())
scale_fill_fb <- function(palette = "deepspec", discrete = TRUE, reverse = FALSE, ...) {
  pal <- fb(palette = palette, reverse = reverse)
  if (discrete) {
    ggplot2::discrete_scale("fill", paste0("fb ",palette," palette"), palette = pal, ...)
  } else {
    ggplot2::scale_fill_gradientn(colours = pal(256), ...)
  }
}


# function to plot palette preview with hex code labels
#' plotpal
#' creates a simple plot to enable a quick look at available palettes and corresponding hex codes. Palettes include: spec, deepspec, lightspec, lighterspec, pinks, pinks2, reds, yellows, greens, greens2, blues, blues2, mono, tonka, bellsprout, dockers, fruitypebbles, day, daylong, and army. Default palette is "deepspec".
#' @param palette name of palette to be used in string format
#'
#' @return
#' @export
#'
#' @examples
#' plotpal(palette = "day")
#' plotpal(palette = "daylong")
plotpal <- function(palette = "deepspec"){
  df <- as.data.frame(t(as.data.frame(fb_pals[[palette]])))
  df$name <- gsub(pattern = '\\.', replacement = ' ', x = rownames(df))
  df$name <- factor(df$name, levels = df$name)
  df$val <- 1
  df$label <- paste0(df$name," - ",df$V1)
  colnames(df) <- c("hex", "name", "val", "label")
  ggplot2::ggplot(df, aes(x = name, y = val, fill = name)) +
    geom_bar(stat = "identity") +
    coord_flip() +
    scale_fill_fb(palette = palette, guide = "none") +
    theme(axis.text.y = element_blank(),
          axis.title = element_blank(),
          panel.background = element_blank(),
          axis.ticks = element_blank(),
          axis.text.x = element_blank()) +
    geom_text(aes(label = label, y = 0.5), size = 4)
}
