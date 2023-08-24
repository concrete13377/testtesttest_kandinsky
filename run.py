import argparse
from pathlib import Path

from PIL import Image

from kandinsky2 import get_kandinsky2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with two path arguments.")
    parser.add_argument("path_img1", help="content img")
    parser.add_argument("path_img2", help="style img")
    parser.add_argument("path_out", help="output dir")
    args = parser.parse_args()

    if not Path(args.path_img1).is_file():
        print(f"{args.path_img1} does not exist")

    if not Path(args.path_img2).is_file():
        print(f"{args.path_img2} does not exist")

    outdir = Path(args.path_out)
    outdir.mkdir(parents=True, exist_ok=True)

    img1 = Image.open(args.path_img1)
    img2 = Image.open(args.path_img2)

    negative_prior_prompt = "nudity, NSFW, lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature"
    model = get_kandinsky2(
        "cuda",
        task_type="text2img",
        cache_dir="/tmp/kandinsky2",
        model_version="2.1",
        use_flash_attention=False,
    )

    image_mixed = model.mix_images(
        [img1, img2],
        [0.5, 0.5],
        num_steps=200,
        batch_size=1,
        guidance_scale=4,
        h=768,
        w=768,
        sampler="p_sampler",
        prior_cf_scale=4,
        prior_steps="5",
        negative_prior_prompt=negative_prior_prompt,
    )

    for idx, i in enumerate(image_mixed):
        i.save(str(outdir / f"mix_result_{idx}.png"))
