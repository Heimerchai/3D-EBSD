def count_lines_in_file(file_path):
    """统计指定文本文件的行数。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

if __name__ == "__main__":
    # 指定文件路径和文件名
    file_path = "/Users/fujiilab_imac_r0309_02/Documents/柴振邦_2022.09.26-/Experiment_results/3D-EBSD/20240619_Helios_5UX/20240619_EBSD/mod_data/Export_mod03/EBSD Mapping_Map_s0097 100 - EBSD Data.ctf"  # 替换为你的文件路径和文件名
    lines = count_lines_in_file(file_path)
    if lines is not None:
        print(f"文件 {file_path} 有 {lines} 行。")
