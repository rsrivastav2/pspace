import React from "react";
import { Dialog, DialogContent } from "@/components/ui/dialog";
import { Progress } from "@/components/ui/progress";

const ProgressModal = ({ open }) => {
  return (
    <Dialog open={open}>
      <DialogContent className="p-6 flex flex-col items-center">
        <p className="text-lg font-semibold mb-4">Processing...</p>
        <Progress value={70} className="w-full" />
      </DialogContent>
    </Dialog>
  );
};

export default ProgressModal;




import React, { useState } from "react";
import ProgressModal from "./ProgressModal";

const MyComponent = () => {
  const [loading, setLoading] = useState(false);

  const test = () => {
    setLoading(true); // Show popup

    setTimeout(() => {
      setLoading(false); // Hide popup after 5 seconds
    }, 5000);
  };

  return (
    <div>
      <button onClick={test} className="px-4 py-2 bg-blue-500 text-white rounded">
        Run Test
      </button>

      <ProgressModal open={loading} />
    </div>
  );
};

export default MyComponent;
