/*
 * Copyright (C) 2012 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.rs.test;

import android.content.Context;
import android.renderscript.RenderScript;

public class UT_atomic extends UnitTest {

    protected UT_atomic(RSTestCore rstc, Context ctx) {
        super(rstc, "Atomics", ctx);
    }

    public void run() {
        RenderScript pRS = RenderScript.create(mCtx);
        ScriptC_atomic s = new ScriptC_atomic(pRS);
        pRS.setMessageHandler(mRsMessage);
        s.invoke_atomic_test();
        pRS.finish();
        waitForMessage();
        s.destroy();
        pRS.destroy();
    }
}
