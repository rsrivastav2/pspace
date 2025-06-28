import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { PieChart, Pie, Cell } from "recharts";

const JobDetails = () => {
  const cpuUsage = 30.5;
  const memoryUsage = 221;
  const cpuData = [
    { name: "Used", value: cpuUsage },
    { name: "Free", value: 100 - cpuUsage },
  ];
  const memData = [
    { name: "Used", value: memoryUsage },
    { name: "Free", value: 1000 - memoryUsage }, // example max memory
  ];

  return (
    <div className="p-6 space-y-6">
      <div className="bg-yellow-100 text-yellow-800 p-4 rounded-xl shadow-md">
        ⚠️ Error: Job Aborted: Manually aborted by user: admin
      </div>

      <Card>
        <CardContent className="grid grid-cols-2 gap-4 p-4">
          <div>
            <div><strong>JOB ID:</strong> jino6d5h202</div>
            <div><strong>EVENT NAME:</strong> Test Event 2</div>
            <div><strong>EVENT TIMING:</strong> Disabled</div>
            <div><strong>CATEGORY NAME:</strong> Test Cat</div>
            <div><strong>PLUGIN NAME:</strong> Test Plugin</div>
            <div><strong>EVENT TARGET:</strong> joeretina.local</div>
          </div>
          <div>
            <div><strong>JOB SOURCE:</strong> Manual (admin)</div>
            <div><strong>SERVER HOSTNAME:</strong> joeretina.local</div>
            <div><strong>PROCESS ID:</strong> 32457</div>
            <div><strong>JOB STARTED:</strong> Apr 30, 2016 11:07 PM</div>
            <div><strong>JOB COMPLETED:</strong> Apr 30, 2016 11:07 PM</div>
            <div><strong>ELAPSED TIME:</strong> 20 seconds</div>
            <Button className="mt-2">Run Again</Button>
          </div>
        </CardContent>
      </Card>

      <div className="grid grid-cols-3 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="text-center font-semibold">Performance Metrics</div>
            <div className="flex justify-center mt-4">
              <PieChart width={100} height={100}>
                <Pie
                  data={[{ name: "total", value: 100 }]} // Static placeholder
                  cx="50%"
                  cy="50%"
                  innerRadius={30}
                  outerRadius={50}
                  fill="#0000FF"
                  dataKey="value"
                />
              </PieChart>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="text-center font-semibold">CPU Usage</div>
            <div className="flex justify-center mt-4">
              <PieChart width={100} height={100}>
                <Pie
                  data={cpuData}
                  cx="50%"
                  cy="50%"
                  innerRadius={30}
                  outerRadius={50}
                  dataKey="value"
                >
                  <Cell fill="#006400" />
                  <Cell fill="#DDDDDD" />
                </Pie>
              </PieChart>
            </div>
            <div className="text-center mt-2">{cpuUsage}% Average</div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="text-center font-semibold">Memory Usage</div>
            <div className="flex justify-center mt-4">
              <PieChart width={100} height={100}>
                <Pie
                  data={memData}
                  cx="50%"
                  cy="50%"
                  innerRadius={30}
                  outerRadius={50}
                  dataKey="value"
                >
                  <Cell fill="#006400" />
                  <Cell fill="#DDDDDD" />
                </Pie>
              </PieChart>
            </div>
            <div className="text-center mt-2">{memoryUsage} MB Average</div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardContent className="p-4">
          <div className="font-semibold mb-2">Job Event Log</div>
          <pre className="bg-gray-100 p-2 rounded text-sm overflow-x-auto">
# Job ID: jino6d5h202
# Event Title: Test Event 2
# Hostname: joeretina.local
# Date/Time: 2016/04/30 23:07:06 (GMT-7)
Printed this with console.warn, should go to stderr...
          </pre>
          <div className="flex gap-4 mt-2">
            <Button variant="outline">Download Log</Button>
            <Button variant="outline">View Full Log</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default JobDetails;
