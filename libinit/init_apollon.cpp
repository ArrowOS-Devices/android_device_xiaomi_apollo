/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_kona.h>

static const variant_info_t apollocn_info = {
    .prop_key = "ro.boot.hwc",
    .prop_value = "CN",

    .brand = "Redmi",
    .device = "apollo",
    .marketname = "K30S Ultra",
    .model = "M2007J3SC",
};

static const variant_info_t apollo_info = {
    .prop_key = "ro.boot.product.hardware.sku",
    .prop_value = "std",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T",
    .model = "M2007J3SY",
};

static const variant_info_t apollopro_info = {
    .prop_key = "ro.boot.product.hardware.sku",
    .prop_value = "pro",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T Pro",
    .model = "M2007J3SG",
};

static const std::vector<variant_info_t> variants = {
    apollocn_info,
    apollo_info,
    apollopro_info,
};

void vendor_load_properties() {
    search_variant(variants);
}
