from utils import *

if __name__ == '__main__':
    mask_path = 'mask.jpg'
    # Load mask image
    mask = load_mask_image(mask_path)

    # Convert mask to binary image
    binary_mask = convert_mask_to_binary(mask, threshold_value=128)

    # Find contours
    contours, hierarchy = cv2.findContours(binary_mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Generate polygons
    polygons = generate_polygons_from_contours(contours, epsilon=0.01)

    polygons = extract_best_fit_quadrilaterals(polygons)

    # Draw polygons on image
    output_image = draw_polygons_on_image(mask, polygons)

    # Resize output image
    output_image = resize_image(output_image, width=800, height=600)

    # Save polygons to JSON file
    save_polygons_to_json(polygons, output_path='polygons.json')

    # Display output image
    cv2.imshow('Output Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
