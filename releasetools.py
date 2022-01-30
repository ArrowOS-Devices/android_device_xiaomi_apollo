# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017-2018 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, basename, dest):
  path = "IMAGES/" + basename
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def OTA_InstallEnd(info):
  info.script.Print("Patching firmware images...")
  AddImage(info, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo")
  AddImage(info, "recovery.img", "/dev/block/bootdevice/by-name/recovery")
  AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")
  AddImage(info, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system")

  fw_cmd = ""

  fw_map = {
      'abl.elf': ['abl'],
      'aop.mbn': ['aop'],
      'BTFM.bin': ['bluetooth'],
      'cmnlib.mbn': ['cmnlib'],
      'cmnlib64.mbn': ['cmnlib64'],
      'devcfg.mbn': ['devcfg'],
      'dspso.bin': ['dsp'],
      'featenabler.mbn': ['featenabler'],
      'hyp.mbn': ['hyp'],
      'km4.mbn': ['keymaster'],
      'NON-HLOS.elf': ['modem'],
      'qupv3fw.elf': ['qupfw'],
      'storsec.mbn': ['storsec'],
      'tz.mbn': ['tz'],
      'uefi_sec.mbn': ['uefisecapp'],
      'xbl_4.elf': ['xbl_4'],
      'xbl_5.elf': ['xbl_5'],
      'xbl_config_4.elf': ['xbl_config_4'],
      'xbl_config_5.elf': ['xbl_config_5']
      }

  # Firmware
  for fw in fw_map.keys():
      for part in fw_map[fw]:
          fw_cmd += 'package_extract_file("install/firmware-update/{}", "/dev/block/bootdevice/by-name/{}");\n'.format(fw, part)
  info.script.AppendExtra(fw_cmd)
