install.packages("plotly")
library(plotly)

# --- ---- Precision y Recall --------------------------------------------------
metricas <- c( "Precisión", "Exhaustividad")
cocoyolo <- c(0.985,0.860)
customyolo <- c(0.991,0.955)
cocomask <- c(0.915,0.943)
custommask <- c(0.995,0.941)
data <- data.frame(metricas, cocoyolo, customyolo, cocomask, custommask)

fig <- plot_ly(data, x = ~metricas, y = ~cocoyolo, type = 'bar', name = 'COCO YOLO')
fig <- fig %>% add_trace(y = ~customyolo, name = 'Custom YOLO' )
fig <- fig %>% add_trace(y = ~cocomask, name = 'COCO Mask RCNN',marker = list(color = "darkslategrey"))
fig <- fig %>% add_trace(y = ~custommask, name = 'Custom Mask RCNN')
fig <- fig %>% layout(yaxis = list(title = 'Observaciones'), xaxis = list(title = 'Métricas'), barmode = 'group')
fig

# --------F - Score ------------------------------------------------------------
fig <- plot_ly(
  x = c("COCO YOLO", "Custom YOLO", "COCO Mask RCNN", "Custom Mask RCNN"),
  y = c(0.918,0.972, 0.928,0.967),
  name = "F-Score",
  type = "bar",
  marker = list(color = c("blue","red","darkslategrey","orange"))
)
fig