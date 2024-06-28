from basic_pitch.inference import predict, predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH

basic_model = Model(ICASSP_2022_MODEL_PATH)


predict_and_save(
    audio_path_list=["sleepy-rain-116521.mp3"],
    output_directory="sample_audio",
    model_or_model_path=basic_model,
    save_midi=True,
    sonify_midi=False,
    save_model_outputs=False,
    save_notes=True
)
