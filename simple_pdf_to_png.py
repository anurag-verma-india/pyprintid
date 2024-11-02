from pdf2image import convert_from_path
import os

def convert_pdf_to_png(input_dir: str, output_dir:str):
    """
    Converts all PDF files in the input directory to PNG images and saves them in the output directory.

    Args:
        input_dir (str): Path to the input directory containing PDF files.
        output_dir (str): Path to the output directory where converted PNG images will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory if it doesn't exist

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)  # Get the full path of the PDF file
            output_path = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.png')  # Construct the output image path

            try:
                # images = convert_from_path(pdf_path, jpegopt="progressive")
                images = convert_from_path(pdf_path, 300)
                for i, img in enumerate(images):
                    img_path = f'{output_path[:-4]}_{i}.png' if i > 0 else output_path  # Add index to output image path if multiple pages
                    img.save(img_path, 'PNG')

            except Exception as e:
                print(f'Error converting {pdf_path}: {e}')

            else:
                print(f'Successfully converted {pdf_path} to {output_path}')


# Change this based on yourn folder paths           
# input_dir="path/of/directory/containing/pdf/files/"
# output_dir="path/of/directory/for/saving/jpg/images/"

if __name__ == "__main__":
    input_dir = "./pdf-files/"
    output_dir= "./png-files"
    convert_pdf_to_png(input_dir, output_dir)
