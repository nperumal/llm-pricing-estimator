{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red16\green16\blue16;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c7451\c7451\c7843;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class GeminiPricing:\
    def __init__(self):\
         self.gemini_flash_prices = \{\
            "image_input_lte_128k": 0.00002, "image_input_gt_128k": 0.00004,\
            "video_input_lte_128k": 0.00002, "video_input_gt_128k": 0.00004,\
            "text_input_lte_128k": 0.00001875, "text_input_gt_128k": 0.0000375,\
            "audio_input_lte_128k": 0.000002, "audio_input_gt_128k": 0.000004,\
            "text_output_lte_128k": 0.000075, "text_output_gt_128k": 0.00015,\
            "tuning_token": 8 / 1000000\
        \}\
\
         self.gemini_pro_prices = \{\
            "image_input_lte_128k": 0.00032875, "image_input_gt_128k": 0.0006575,\
            "video_input_lte_128k": 0.00032875, "video_input_gt_128k": 0.0006575,\
            "text_input_lte_128k": 0.0003125, "text_input_gt_128k": 0.000625,\
            "audio_input_lte_128k": 0.00003125, "audio_input_gt_128k": 0.0000625,\
            "text_output_lte_128k": 0.00125, "text_output_gt_128k": 0.0025,\
             "tuning_token": 80 / 1000000\
        \}\
\
         self.gemini_1_pro_prices = \{\
            "image_input": 0.0025,\
            "video_input": 0.002,\
            "text_input": 0.000125,\
            "text_output": 0.000375\
        \}\
         self.grounding_price = 35 / 1000\
         self.cached_input_flash_prices = \{\
            "image_input_lte_128k": 0.000005, "image_input_gt_128k": 0.00001,\
            "video_input_lte_128k": 0.000005, "video_input_gt_128k": 0.00001,\
            "text_input_lte_128k": 0.0000046875, "text_input_gt_128k": 0.000009375,\
            "audio_input_lte_128k": 0.0000005, "audio_input_gt_128k": 0.000001,\
        \}\
         self.context_storage_flash_prices = \{\
           "image_input": 0.000263,\
            "video_input": 0.000263,\
            "text_input": 0.00025,\
            "audio_input": 0.000025\
        \}\
         self.cached_input_pro_prices = \{\
            "image_input_lte_128k": 0.0000821875, "image_input_gt_128k": 0.000164375,\
            "video_input_lte_128k": 0.0000821875, "video_input_gt_128k": 0.000164375,\
            "text_input_lte_128k": 0.000078125, "text_input_gt_128k": 0.00015625,\
            "audio_input_lte_128k": 0.0000078125, "audio_input_gt_128k": 0.000015625,\
        \}\
\
         self.context_storage_pro_prices = \{\
            "image_input": 0.0011835,\
            "video_input": 0.0011835,\
            "text_input": 0.001125,\
             "audio_input": 0.0001125\
        \}\
\
\
    def calculate_inference_cost(self, model_type, input_data, output_data, data_type, context_length = 0):\
        total_cost = 0\
        if model_type == "Gemini 1.5 Flash":\
             if data_type == "text":\
                 input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                 output_cost_key = "text_output_lte_128k" if context_length <= 128000 else "text_output_gt_128k"\
                 total_cost = (input_data / 1000 * self.gemini_flash_prices[input_cost_key]) + \\\
                               (output_data / 1000 * self.gemini_flash_prices[output_cost_key])\
             elif data_type == "image":\
                 input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                 total_cost = input_data * self.gemini_flash_prices[input_cost_key]\
             elif data_type == "video":\
                input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                total_cost = input_data * self.gemini_flash_prices[input_cost_key]\
             elif data_type == "audio":\
                input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                total_cost = input_data * self.gemini_flash_prices[input_cost_key]\
\
\
        elif model_type == "Gemini 1.5 Pro":\
             if data_type == "text":\
                 input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                 output_cost_key = "text_output_lte_128k" if context_length <= 128000 else "text_output_gt_128k"\
                 total_cost = (input_data / 1000 * self.gemini_pro_prices[input_cost_key]) + \\\
                               (output_data / 1000 * self.gemini_pro_prices[output_cost_key])\
             elif data_type == "image":\
                 input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                 total_cost = input_data * self.gemini_pro_prices[input_cost_key]\
             elif data_type == "video":\
                input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                total_cost = input_data * self.gemini_pro_prices[input_cost_key]\
             elif data_type == "audio":\
                input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                total_cost = input_data * self.gemini_pro_prices[input_cost_key]\
\
        elif model_type == "Gemini 1.0 Pro":\
             if data_type == "text":\
                  total_cost = (input_data / 1000 * self.gemini_1_pro_prices["text_input"]) + (output_data / 1000 * self.gemini_1_pro_prices["text_output"])\
             elif data_type == "image":\
                  total_cost = input_data * self.gemini_1_pro_prices["image_input"]\
             elif data_type == "video":\
                  total_cost = input_data * self.gemini_1_pro_prices["video_input"]\
        return total_cost\
\
    def calculate_fine_tuning_cost(self, model_type, training_tokens):\
        if model_type == "Gemini 1.5 Flash":\
            return training_tokens * self.gemini_flash_prices["tuning_token"]\
        elif model_type == "Gemini 1.5 Pro":\
              return training_tokens * self.gemini_pro_prices["tuning_token"]\
        return 0\
\
    def calculate_grounding_cost(self, num_requests):\
        return num_requests / 1000 * self.grounding_price\
    def calculate_cached_cost(self,model_type,  input_data, output_data, data_type, cache_context, ttl_hours, num_requests, context_length = 0 ):\
        total_cost = 0\
        if model_type == "Gemini 1.5 Flash":\
\
            if data_type == "text":\
                cache_input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                cached_input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                storage_cost_key = "text_input"\
                cache_creation_cost = cache_context/ 1000 * self.gemini_flash_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours / 1000 * self.context_storage_flash_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests / 1000 * self.cached_input_flash_prices[cached_input_cost_key])\
                new_input_cost = input_data / 1000 * self.gemini_flash_prices[cache_input_cost_key]\
                output_cost_key = "text_output_lte_128k" if context_length <= 128000 else "text_output_gt_128k"\
                output_cost = output_data / 1000 * self.gemini_flash_prices[output_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost + output_cost\
\
\
            elif data_type == "image":\
                cache_input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                cached_input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                storage_cost_key = "image_input"\
                cache_creation_cost = cache_context * self.gemini_flash_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_flash_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests *  self.cached_input_flash_prices[cached_input_cost_key])\
                new_input_cost = input_data  * self.gemini_flash_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
\
            elif data_type == "video":\
                cache_input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                cached_input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                storage_cost_key = "video_input"\
                cache_creation_cost = cache_context * self.gemini_flash_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_flash_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests * self.cached_input_flash_prices[cached_input_cost_key])\
                new_input_cost = input_data * self.gemini_flash_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
            elif data_type == "audio":\
                cache_input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                cached_input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                storage_cost_key = "audio_input"\
                cache_creation_cost = cache_context * self.gemini_flash_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_flash_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests * self.cached_input_flash_prices[cached_input_cost_key])\
                new_input_cost = input_data  * self.gemini_flash_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
\
\
        elif model_type == "Gemini 1.5 Pro":\
             if data_type == "text":\
                cache_input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                cached_input_cost_key = "text_input_lte_128k" if context_length <= 128000 else "text_input_gt_128k"\
                storage_cost_key = "text_input"\
                cache_creation_cost = cache_context/ 1000 * self.gemini_pro_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours / 1000 * self.context_storage_pro_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests / 1000 * self.cached_input_pro_prices[cached_input_cost_key])\
                new_input_cost = input_data / 1000 * self.gemini_pro_prices[cache_input_cost_key]\
                output_cost_key = "text_output_lte_128k" if context_length <= 128000 else "text_output_gt_128k"\
                output_cost = output_data / 1000 * self.gemini_pro_prices[output_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost + output_cost\
             elif data_type == "image":\
                cache_input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                cached_input_cost_key = "image_input_lte_128k" if context_length <= 128000 else "image_input_gt_128k"\
                storage_cost_key = "image_input"\
                cache_creation_cost = cache_context * self.gemini_pro_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_pro_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests *  self.cached_input_pro_prices[cached_input_cost_key])\
                new_input_cost = input_data  * self.gemini_pro_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
\
             elif data_type == "video":\
                cache_input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                cached_input_cost_key = "video_input_lte_128k" if context_length <= 128000 else "video_input_gt_128k"\
                storage_cost_key = "video_input"\
                cache_creation_cost = cache_context * self.gemini_pro_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_pro_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests * self.cached_input_pro_prices[cached_input_cost_key])\
                new_input_cost = input_data * self.gemini_pro_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
             elif data_type == "audio":\
                cache_input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                cached_input_cost_key = "audio_input_lte_128k" if context_length <= 128000 else "audio_input_gt_128k"\
                storage_cost_key = "audio_input"\
                cache_creation_cost = cache_context * self.gemini_pro_prices[cache_input_cost_key]\
                cache_storage_cost = cache_context * ttl_hours * self.context_storage_pro_prices[storage_cost_key]\
                cached_input_cost = (cache_context * num_requests * self.cached_input_pro_prices[cached_input_cost_key])\
                new_input_cost = input_data  * self.gemini_pro_prices[cache_input_cost_key]\
                total_cost = cache_creation_cost + cache_storage_cost + cached_input_cost + new_input_cost\
        return total_cost\
class ImagenPricing:\
    def __init__(self):\
        self.imagen_prices = \{\
            "imagen3": 0.04,\
            "imagen3_fast": 0.02,\
            "imagen2": 0.020,\
            "image_edit": 0.020,\
            "upscaling": 0.003,\
            "visual_captioning": 0.0015,\
            "visual_qa": 0.0015,\
\
        \}\
\
    def calculate_image_generation_cost(self, model_type, num_images):\
        if model_type in self.imagen_prices:\
            return num_images * self.imagen_prices[model_type]\
        return 0\
\
    def calculate_image_editing_cost(self, num_images):\
         return num_images * self.imagen_prices["image_edit"]\
\
    def calculate_upscaling_cost(self, num_images):\
        return num_images * self.imagen_prices["upscaling"]\
    def calculate_visual_captioning_cost(self, num_images):\
         return num_images * self.imagen_prices["visual_captioning"]\
    def calculate_visual_qa_cost(self, num_images):\
         return num_images * self.imagen_prices["visual_qa"]\
\
\
    def calculate_fine_tuning_cost(self, node_hours):\
         # Vertex AI custom training pricing not given, provide a placeholder\
        return node_hours * 10 #Placeholder, replace with actual pricing\
\
class EmbeddingPricing:\
    def __init__(self):\
        self.embedding_prices = \{\
            "text_input": 0.0002/1000,\
            "image_input": 0.0001,\
            "video_plus": 0.0020,\
            "video_standard": 0.0010,\
            "video_essential": 0.0005,\
            "text_input_online": 0.000025/1000,\
            "text_input_batch": 0.00002/1000\
         \}\
\
    def calculate_embedding_cost(self, data_type, input_data, model_type = None, request_type = None):\
         if data_type == "text" and request_type == "online":\
             return  input_data * self.embedding_prices["text_input_online"]\
\
         elif data_type == "text" and request_type == "batch":\
            return  input_data * self.embedding_prices["text_input_batch"]\
\
         elif data_type == "text":\
            return  input_data * self.embedding_prices["text_input"]\
\
         elif data_type == "image":\
            return  input_data * self.embedding_prices["image_input"]\
         elif data_type == "video":\
            if model_type == "Video Plus":\
                return input_data * self.embedding_prices["video_plus"]\
            elif model_type == "Video Standard":\
                 return input_data * self.embedding_prices["video_standard"]\
            elif model_type == "Video Essential":\
                 return input_data * self.embedding_prices["video_essential"]\
         return 0\
\
class CodeCompletionPricing:\
    def __init__(self):\
        self.code_completion_prices = \{\
            "input": 0.00025/1000,\
            "output": 0.0005/1000\
        \}\
    def calculate_code_completion_cost(self, input_chars, output_chars):\
        input_cost = input_chars * self.code_completion_prices["input"]\
        output_cost = output_chars * self.code_completion_prices["output"]\
        return input_cost + output_cost\
\
class TranslationPricing:\
    def __init__(self):\
        self.translation_prices = \{\
            "input": 10 / 1000000,\
            "output": 10 / 1000000\
        \}\
    def calculate_translation_cost(self, input_chars, output_chars):\
         input_cost = input_chars * self.translation_prices["input"]\
         output_cost = output_chars * self.translation_prices["output"]\
         return input_cost + output_cost\
class PartnerModelPricing:\
    def __init__(self):\
        self.partner_model_prices = \{\
            "jamba_1_5_large_input": 2 / 1000000,\
            "jamba_1_5_large_output": 8 / 1000000,\
            "jamba_1_5_mini_input": 0.20 / 1000000,\
            "jamba_1_5_mini_output": 0.40 / 1000000,\
             "claude_3_5_haiku_input": 0.80/1000000,\
             "claude_3_5_haiku_output": 4 / 1000000,\
             "claude_3_5_haiku_batch_input": 0.40/1000000,\
             "claude_3_5_haiku_batch_output": 2 / 1000000,\
             "claude_3_5_haiku_cache_write": 1 / 1000000,\
              "claude_3_5_haiku_cache_hit": 0.08 / 1000000,\
              "claude_3_5_haiku_batch_cache_write": 0.50/1000000,\
             "claude_3_5_haiku_batch_cache_hit": 0.04 / 1000000,\
             "claude_3_5_sonnet_v2_input": 3 / 1000000,\
             "claude_3_5_sonnet_v2_output": 15 / 1000000,\
             "claude_3_5_sonnet_v2_batch_input": 1.50/1000000,\
             "claude_3_5_sonnet_v2_batch_output": 7.50 / 1000000,\
             "claude_3_5_sonnet_v2_cache_write": 3.75 / 1000000,\
              "claude_3_5_sonnet_v2_cache_hit": 0.30 / 1000000,\
              "claude_3_5_sonnet_v2_batch_cache_write": 1.875/1000000,\
             "claude_3_5_sonnet_v2_batch_cache_hit": 0.15 / 1000000,\
\
            "claude_3_5_sonnet_input": 3/1000000,\
            "claude_3_5_sonnet_output": 15 / 1000000,\
             "claude_3_haiku_input": 0.25 / 1000000,\
            "claude_3_haiku_output": 1.25/1000000,\
             "claude_3_sonnet_input": 3/1000000,\
            "claude_3_sonnet_output": 15 / 1000000,\
            "claude_3_opus_input": 15 / 1000000,\
            "claude_3_opus_output": 75/1000000,\
            "llama_3_405b_input": 5 / 1000000,\
             "llama_3_405b_output": 16/1000000,\
              "mistral_large_24_11_input": 2 / 1000000,\
              "mistral_large_24_11_output": 6/1000000,\
              "mistral_large_24_07_input": 2 / 1000000,\
             "mistral_large_24_07_output": 6/1000000,\
               "mistral_nemo_input": 0.15/1000000,\
               "mistral_nemo_output": 0.15/1000000,\
               "codestral_24_05_input": 0.20/1000000,\
               "codestral_24_05_output": 0.60/1000000\
\
        \}\
    def calculate_partner_model_cost(self, model_type, input_tokens, output_tokens, request_type=None):\
        total_cost = 0\
        if model_type == "Jamba 1.5 Large":\
            total_cost = (input_tokens * self.partner_model_prices["jamba_1_5_large_input"]) + (output_tokens * self.partner_model_prices["jamba_1_5_large_output"])\
\
        elif model_type == "Jamba 1.5 Mini":\
             total_cost = (input_tokens * self.partner_model_prices["jamba_1_5_mini_input"]) + (output_tokens * self.partner_model_prices["jamba_1_5_mini_output"])\
\
        elif model_type == "Claude 3.5 Haiku":\
            if request_type == "batch":\
                total_cost = (input_tokens * self.partner_model_prices["claude_3_5_haiku_batch_input"]) + (output_tokens * self.partner_model_prices["claude_3_5_haiku_batch_output"])\
\
            else:\
               total_cost = (input_tokens * self.partner_model_prices["claude_3_5_haiku_input"]) + (output_tokens * self.partner_model\
}