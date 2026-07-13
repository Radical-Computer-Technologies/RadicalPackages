/*
 @licstart  The following is the entire license notice for the JavaScript code in this file.

 The MIT License (MIT)

 Copyright (C) 1997-2020 by Dimitri van Heesch

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 and associated documentation files (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge, publish, distribute,
 sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @licend  The above is the entire license notice for the JavaScript code in this file
*/
var NAVTREE =
[
  [ "RADix-OS Kernel", "index.html", [
    [ "RADix-OS Kernel API", "index.html", [
      [ "Start Here", "index.html#autotoc_md32", null ],
      [ "API Groups", "index.html#autotoc_md33", null ],
      [ "Filesystem Profile", "index.html#autotoc_md34", null ],
      [ "Verification", "index.html#autotoc_md35", null ]
    ] ],
    [ "RADix Platform Layout", "md__media_jvincent_Kingspec512_repos_RADix_OS_RADixKernel_platforms_README.html", null ],
    [ "API Groups", "api_groups.html", [
      [ "Kernel And Boot", "api_groups.html#autotoc_md1", null ],
      [ "Time, Tasks, And Synchronization", "api_groups.html#autotoc_md2", null ],
      [ "POSIX-Inspired Runtime", "api_groups.html#autotoc_md3", null ],
      [ "Device Model", "api_groups.html#autotoc_md4", null ],
      [ "Networking", "api_groups.html#autotoc_md5", null ],
      [ "Driver Binding", "api_groups.html#autotoc_md6", null ],
      [ "Overlay Tree And IRQs", "api_groups.html#autotoc_md7", null ],
      [ "Display And Input", "api_groups.html#autotoc_md8", null ],
      [ "Experimental Compositor", "api_groups.html#autotoc_md9", null ]
    ] ],
    [ "API Structure", "api_structure.html", [
      [ "Initialization And Boot", "api_structure.html#autotoc_md10", null ],
      [ "Runtime Services", "api_structure.html#autotoc_md11", null ],
      [ "Platform Layout", "api_structure.html#autotoc_md12", null ],
      [ "Handle Rules", "api_structure.html#autotoc_md13", null ],
      [ "Crimson Stability", "api_structure.html#autotoc_md14", null ]
    ] ],
    [ "Crimson 0.1.0 Status", "crimson_status.html", [
      [ "Stable-Beta Surface", "crimson_status.html#autotoc_md15", null ],
      [ "Experimental Surface", "crimson_status.html#autotoc_md16", null ],
      [ "Not Yet Complete", "crimson_status.html#autotoc_md17", null ]
    ] ],
    [ "Overlay And Device Tree Guide", "device_tree_guide.html", [
      [ "Overlay Shape", "device_tree_guide.html#autotoc_md18", null ],
      [ "Bus And Device Binding", "device_tree_guide.html#autotoc_md19", null ],
      [ "Interrupt Domains", "device_tree_guide.html#autotoc_md20", null ],
      [ "Framebuffer Outputs", "device_tree_guide.html#autotoc_md21", null ],
      [ "Boot Services", "device_tree_guide.html#autotoc_md22", null ],
      [ "Current Limits", "device_tree_guide.html#autotoc_md23", null ]
    ] ],
    [ "Minimal Examples", "minimal_examples.html", [
      [ "Register A Kernel Module", "minimal_examples.html#autotoc_md24", null ],
      [ "Register An I2C Controller And Child Driver", "minimal_examples.html#autotoc_md25", null ],
      [ "Register DMA And Use SPI Auto Mode", "minimal_examples.html#autotoc_md26", null ],
      [ "Register A Framebuffer", "minimal_examples.html#autotoc_md27", null ],
      [ "Read Input Events", "minimal_examples.html#autotoc_md28", null ],
      [ "Mount A VFS Provider", "minimal_examples.html#autotoc_md29", null ],
      [ "Use File Descriptors Through The Syscall ABI", "minimal_examples.html#autotoc_md30", null ]
    ] ],
    [ "Experimental Networking", "networking.html", [
      [ "Current Stack", "networking.html#autotoc_md36", null ],
      [ "Current Limits", "networking.html#autotoc_md37", null ],
      [ "Verification", "networking.html#autotoc_md38", null ]
    ] ],
    [ "Pi Zero 2 W Bring-Up", "pi_zero2w.html", [
      [ "Required Loader State", "pi_zero2w.html#autotoc_md39", null ],
      [ "Current Payload", "pi_zero2w.html#autotoc_md40", null ],
      [ "Circle Loader Gate", "pi_zero2w.html#autotoc_md41", null ],
      [ "Current Limits", "pi_zero2w.html#autotoc_md42", null ]
    ] ],
    [ "RadBuild Integration", "radbuild_integration.html", [
      [ "Build Command", "radbuild_integration.html#autotoc_md43", null ],
      [ "Artifact Output", "radbuild_integration.html#autotoc_md44", null ],
      [ "Publication", "radbuild_integration.html#autotoc_md45", null ]
    ] ],
    [ "RADCompositor", "radcompositor.html", [
      [ "Architecture", "radcompositor.html#autotoc_md46", null ],
      [ "Shared-Memory IPC", "radcompositor.html#autotoc_md47", null ],
      [ "Current Limits", "radcompositor.html#autotoc_md48", null ],
      [ "Verification", "radcompositor.html#autotoc_md49", null ]
    ] ],
    [ "Classes", "annotated.html", [
      [ "Class List", "annotated.html", "annotated_dup" ],
      [ "Class Index", "classes.html", null ],
      [ "Class Members", "functions.html", [
        [ "All", "functions.html", "functions_dup" ],
        [ "Functions", "functions_func.html", null ],
        [ "Variables", "functions_vars.html", "functions_vars" ]
      ] ]
    ] ],
    [ "Files", "files.html", [
      [ "File List", "files.html", "files_dup" ],
      [ "File Members", "globals.html", [
        [ "All", "globals.html", "globals_dup" ],
        [ "Functions", "globals_func.html", "globals_func" ],
        [ "Typedefs", "globals_type.html", null ],
        [ "Enumerations", "globals_enum.html", null ],
        [ "Enumerator", "globals_eval.html", null ],
        [ "Macros", "globals_defs.html", null ]
      ] ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"annotated.html",
"radixkernel_8h.html#a05c5d60a6604ffe8e3f2c13292305504a292a76e15758ab5e1756eededed084ac",
"radixkernel_8h.html#a71b5a6ce065927acf22a8fb4e403de9fa9af3c655235c32b77ef8d5b1de428454",
"radixkernel_8h.html#ab50b14550381993540d9ee0868a75de7",
"structrad__a53__capabilities.html#aa73f525511c1bb8a7f2e053ba9ffb5f0",
"structrad__irq__domain__config.html#a044778c740b065e11888ba8c37ca4135",
"structrad__timer__source__info.html"
];

var SYNCONMSG = 'click to disable panel synchronisation';
var SYNCOFFMSG = 'click to enable panel synchronisation';