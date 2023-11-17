import gradio as gr
from controlnet_aux import SamDetector

sam = SamDetector.from_pretrained("ybelkada/segment-anything", subfolder="checkpoints")


def image_processing_app(input_image):
    # Process the input image
    processed_image_sam = sam(input_image)

    return processed_image_sam


# Create a Gradio interface
iface = gr.Interface(fn=image_processing_app, inputs="image", outputs="image", title="Image Processing App")

# Launch the interface
iface.launch()
