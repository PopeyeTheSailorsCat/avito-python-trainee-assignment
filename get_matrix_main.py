from typing import List
import aiohttp
import asyncio
import logging


async def matrix_request(url: str) -> str:
    """
    This function send request to url and get text part of response
    :param url:
    :return: html_text
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status % 100 == 5:  # Server errors
                    logging.error(response.status)
                    raise ConnectionError

                html_text = await response.text()
                return html_text
        except ConnectionError:
            logging.error("No response")
            raise ConnectionError


def get_matrix_spiral(matrix: List[List[int]]) -> List[int]:
    """
    In this function we run algo to get spiral path of matrix
    :param matrix: parsed matrix from response.text
    :return: path
    """
    path = []
    layer = 0  # our current depth
    i = j = 0
    size = len(matrix)

    while True:
        path.extend([matrix[i][j] for i in range(layer, size - layer)])  # down
        if len(path) == size * size:  # not even size stops here
            break
        i = size - layer - 1

        path.extend([matrix[i][j] for j in range(layer + 1, size - layer)])  # right
        j = size - layer - 1

        path.extend([matrix[i][j] for i in range(size - layer - 2, layer - 1, -1)])  # up
        i = layer

        if len(path) == size * size:  # if size is even it will stop here.
            break

        layer += 1  # increase our depth

        path.extend([matrix[i][j] for j in range(size - layer - 1, layer - 1, -1)])  # left
        j = layer

    return path


def parse_matrix_from_str(text_matrix: str) -> List[List[int]]:
    """
    In this function we get matrix from text response
    :param text_matrix:
    :return:
    """
    lines = text_matrix.split("\n")
    matrix = []
    for line in lines:
        if len(line) == 0 or line[0] == "+":  # plus means useless
            continue
        matrix_line = [int(element) for element in line[1:-1].split(" | ")]  # [1:-1] drop | start and end of lines
        matrix.append(matrix_line)
    return matrix


async def get_matrix(url: str) -> List[int]:
    try:
        response_text = await matrix_request(url)  # get text of matrix
    except ConnectionError as ex:
        logging.warning("Connection Error occurred")
        return []

    matrix = parse_matrix_from_str(response_text)  # get matrix from text
    return get_matrix_spiral(matrix)  # run algo


if __name__ == "__main__":
    SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_matrix(SOURCE_URL))
