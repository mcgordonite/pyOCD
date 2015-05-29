"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash_kinetis import Flash_Kinetis

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4604b570, 0x4616460d, 0x5020f24c, 0x81c84932, 0x1028f64d, 0x460881c8, 0xf0208800, 0x80080001,
    0x4448482e, 0xf8dcf000, 0x2001b108, 0x2000bd70, 0x4601e7fc, 0x47702000, 0x4929b510, 0x44484827,
    0xf8b8f000, 0xb92c4604, 0x48242100, 0xf0004448, 0x4604f9a3, 0xf837f000, 0xbd104620, 0x4604b570,
    0x4448481e, 0x46214b1e, 0xf00068c2, 0x4605f85d, 0x481ab93d, 0x23004448, 0x68c24621, 0xf940f000,
    0xf0004605, 0x4628f820, 0xb5febd70, 0x460c4605, 0x46234616, 0x46294632, 0x44484810, 0xf8f8f000,
    0xb9674607, 0x22012000, 0x2000e9cd, 0x46224633, 0x90024629, 0x44484809, 0xf97ef000, 0xf0004607,
    0x4638f802, 0x4807bdfe, 0xf4206840, 0xf5000070, 0x49040070, 0x47706048, 0x40052000, 0x00000004,
    0x6b65666b, 0x4001f000, 0x4a0e2070, 0x20807010, 0xbf007010, 0x7800480b, 0x280009c0, 0x4809d0fa,
    0xf0017801, 0xb1080020, 0x47702067, 0x0010f001, 0x2068b108, 0xf001e7f9, 0xb1080001, 0xe7f42069,
    0xe7f22000, 0x40020000, 0x4df0e92d, 0x460d4604, 0x469a4690, 0xf0004650, 0x4606f891, 0x4630b116,
    0x8df0e8bd, 0x46422304, 0x46204629, 0xf86cf000, 0xb10e4606, 0xe7f34630, 0x0008eb05, 0x68e01e47,
    0xf1f0fbb7, 0x7011fb00, 0x68e0b140, 0xf0f0fbb7, 0x0b01f100, 0xfb0068e0, 0x1e47f00b, 0x480be011,
    0x68004478, 0x20096005, 0x71c84909, 0xffacf7ff, 0x69a04606, 0x69a0b108, 0xb1064780, 0x68e0e003,
    0x42bd4405, 0xbf00d9eb, 0xe7c94630, 0x000002e0, 0x40020000, 0x4604b570, 0x4628460d, 0xf84ef000,
    0xb10e4606, 0xbd704630, 0x2004b90c, 0x2044e7fb, 0x71c84902, 0xff88f7ff, 0x0000e7f5, 0x40020000,
    0xb9094601, 0x47702004, 0x6cc04826, 0x6003f3c0, 0x447b4b25, 0x0010f833, 0xb90a0302, 0xe7f22064,
    0x60082000, 0x2001604a, 0x02806088, 0x200060c8, 0x61486108, 0xbf006188, 0x4602e7e5, 0x2004b90a,
    0x61914770, 0xe7fb2000, 0x4604b530, 0x2004b90c, 0x1e58bd30, 0xb9104008, 0x40101e58, 0x2065b108,
    0x6820e7f6, 0xd8054288, 0x0500e9d4, 0x188d4428, 0xd20142a8, 0xe7eb2066, 0xe7e92000, 0x480b4601,
    0xd0014281, 0x4770206b, 0xe7fc2000, 0xb90b4603, 0x47702004, 0xd801290f, 0xd0012a04, 0xe7f82004,
    0xe7f62000, 0x40048000, 0x0000024e, 0x6b65666b, 0x41f0e92d, 0x46884607, 0x461d4614, 0x2004b914,
    0x81f0e8bd, 0x462a2304, 0x46384641, 0xffbcf7ff, 0xb10e4606, 0xe7f34630, 0x480fe019, 0x68004478,
    0x8000f8c0, 0x490ccc01, 0x390c4479, 0x60486809, 0x490a2006, 0xf7ff71c8, 0x4606ff07, 0xb10869b8,
    0x478069b8, 0xe004b106, 0x0804f108, 0x2d001f2d, 0xbf00d1e3, 0xe7d34630, 0x000001a4, 0x40020000,
    0x4dffe92d, 0x4682b082, 0x2304460c, 0x46504621, 0xf7ff9a04, 0x4683ff89, 0x0f00f1bb, 0x4658d003,
    0xe8bdb006, 0xe9da8df0, 0xfbb00101, 0x4260f7f1, 0x40084279, 0x42a54245, 0x443dd100, 0xe0229e04,
    0x0804eba5, 0xd90045b0, 0xea4f46b0, 0x90010098, 0x4478480f, 0x60046800, 0x490e2001, 0x980171c8,
    0x72c80a00, 0x72889801, 0x72489805, 0xfebcf7ff, 0xf1bb4683, 0xd0010f00, 0xe7d14658, 0x0608eba6,
    0x443d4444, 0x2e00bf00, 0x2000d1da, 0x0000e7c8, 0x0000010e, 0x40020000, 0x4604b570, 0xb90c460d,
    0xbd702004, 0x49032040, 0x460871c8, 0xf7ff7185, 0xe7f6fe9b, 0x40020000, 0x4dffe92d, 0x4617460c,
    0xe9dd461d, 0xf8ddb80c, 0xb91da038, 0xb0042004, 0x8df0e8bd, 0x463a2304, 0x98004621, 0xff24f7ff,
    0xb10e4606, 0xe7f24630, 0x4814e022, 0x68004478, 0x20026004, 0x71c84912, 0xf8804608, 0x490fb00b,
    0x39144479, 0x68096828, 0xf7ff6088, 0x4606fe6d, 0xf1b8b15e, 0xd0010f00, 0x4000f8c8, 0x0f00f1ba,
    0x2000d002, 0x0000f8ca, 0x1f3fe004, 0x1d241d2d, 0xd1da2f00, 0x4630bf00, 0x0000e7c9, 0x00000074,
    0x40020000, 0x00000000, 0x00080000, 0x00100000, 0x00200000, 0x00400000, 0x00800000, 0x01000000,
    0x01000000, 0x40020004, 0x00000000,
                                ],
               'pc_init' : 0x20000021,
               'pc_eraseAll' : 0x20000059,
               'pc_erase_sector' : 0x2000007D,
               'pc_program_page' : 0x200000AB,
               'begin_stack' : 0x20000c00,
               'begin_data' : 0x20001c00,       # Analyzer uses a max of 512 B data (128 pages * 4 bytes / page)
               'page_buffers' : [0x20001800, 0x20001c00],   # Enable double buffering
               'static_base' : 0x20000000 + 0x20 + 0x468,
               'page_size' : 1024,
               'analyzer_supported' : True,
               'analyzer_address' : 0x1fffe000  # Analyzer 0x1fffe000..0x1fffe600
              };

class Flash_k20d50m(Flash_Kinetis):

    def __init__(self, target):
        super(Flash_k20d50m, self).__init__(target, flash_algo)

