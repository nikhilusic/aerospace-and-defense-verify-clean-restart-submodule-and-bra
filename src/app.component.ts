import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

type AlertSeverity = 'warning' | 'info';
type TimelineStatus = 'done' | 'in-progress' | 'queued';

interface Metric {
  label: string;
  value: number | string;
  delta: string;
}

interface TrendPoint {
  label: string;
  value: number;
}

interface BreakdownItem {
  label: string;
  value: number;
}

interface TimelineItem {
  step: string;
  eta: string;
  status: TimelineStatus;
}

interface AlertItem {
  severity: AlertSeverity;
  message: string;
}

interface RecordItem {
  id: string;
  name: string;
  status: string;
  owner: string;
}

interface BlueprintScreen {
  id: string;
  title: string;
  role: string;
  action: string;
  route: string;
  requirements: string[];
  mockData: {
    metrics: Metric[];
    trendSeries: TrendPoint[];
    breakdown: BreakdownItem[];
    timeline: TimelineItem[];
    alerts: AlertItem[];
    records: RecordItem[];
    routeHint: string;
  };
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  readonly title = 'Aerospace & Defense Resource Management';
  readonly projectContext = 'Create a end to end resource management application for the selected industry domain';
  readonly timeWindow = 'Last 8 weeks';
  readonly screens: BlueprintScreen[] = [
    {
      id: 'dashboard',
      title: 'Resource Command Center',
      role: 'Primary User',
      action: 'Program readiness and compliance posture',
      route: '/mockup-1',
      requirements: [
        'Certification tasks due this month · Selected',
        'Open safety hazards by criticality · Industry',
        'Subsystem verification progress · Domain'
      ],
      mockData: {
        metrics: [
          { label: 'Open Items', value: 92, delta: '+3%' },
          { label: 'SLA Risk', value: 4, delta: '1 down' },
          { label: 'Flow Health', value: '93%', delta: '+1%' }
        ],
        trendSeries: [
          { label: 'W1', value: 56 },
          { label: 'W2', value: 60 },
          { label: 'W3', value: 65 },
          { label: 'W4', value: 71 },
          { label: 'W5', value: 77 }
        ],
        breakdown: [
          { label: 'Program', value: 35 },
          { label: 'Engineering', value: 30 },
          { label: 'Operations', value: 20 },
          { label: 'Compliance', value: 15 }
        ],
        timeline: [
          { step: 'Intake', eta: '10 min', status: 'done' },
          { step: 'Review', eta: '25 min', status: 'in-progress' },
          { step: 'Approval', eta: '40 min', status: 'queued' }
        ],
        alerts: [
          { severity: 'warning', message: 'Resource Command Center: threshold alert requires follow-up' },
          { severity: 'info', message: 'Resource Command Center: pipeline synchronized successfully' }
        ],
        records: [
          { id: 'RESOURCE-COMMAND-CENTER-101', name: 'Resource Command Center primary item', status: 'In Review', owner: 'Product Lead' },
          { id: 'RESOURCE-COMMAND-CENTER-102', name: 'Resource Command Center validation item', status: 'Pending', owner: 'Ops Manager' },
          { id: 'RESOURCE-COMMAND-CENTER-103', name: 'Resource Command Center compliance item', status: 'Escalated', owner: 'Compliance Owner' }
        ],
        routeHint: '/mockup-1'
      }
    },
    {
      id: 'workspace',
      title: 'Selected Workflow Studio',
      role: 'Primary User',
      action: 'Requirement-to-test execution control',
      route: '/mockup-2',
      requirements: [
        'Create verification package · Industry',
        'Route test evidence for review · Domain',
        'Resolve failed requirement trace links · Resource'
      ],
      mockData: {
        metrics: [
          { label: 'Open Items', value: 104, delta: '+4%' },
          { label: 'SLA Risk', value: 5, delta: '1 down' },
          { label: 'Flow Health', value: '94%', delta: '+2%' }
        ],
        trendSeries: [
          { label: 'W1', value: 64 },
          { label: 'W2', value: 68 },
          { label: 'W3', value: 73 },
          { label: 'W4', value: 79 },
          { label: 'W5', value: 85 }
        ],
        breakdown: [
          { label: 'Program', value: 35 },
          { label: 'Engineering', value: 30 },
          { label: 'Operations', value: 20 },
          { label: 'Compliance', value: 15 }
        ],
        timeline: [
          { step: 'Intake', eta: '10 min', status: 'done' },
          { step: 'Review', eta: '25 min', status: 'in-progress' },
          { step: 'Approval', eta: '40 min', status: 'queued' }
        ],
        alerts: [
          { severity: 'warning', message: 'Selected Workflow Studio: threshold alert requires follow-up' },
          { severity: 'info', message: 'Selected Workflow Studio: pipeline synchronized successfully' }
        ],
        records: [
          { id: 'SELECTED-WORKFLOW-STUDIO-102', name: 'Selected Workflow Studio primary item', status: 'In Review', owner: 'Product Lead' },
          { id: 'SELECTED-WORKFLOW-STUDIO-103', name: 'Selected Workflow Studio validation item', status: 'Pending', owner: 'Ops Manager' },
          { id: 'SELECTED-WORKFLOW-STUDIO-104', name: 'Selected Workflow Studio compliance item', status: 'Escalated', owner: 'Compliance Owner' }
        ],
        routeHint: '/mockup-2'
      }
    },
    {
      id: 'insights',
      title: 'Industry Insight Radar',
      role: 'Primary User',
      action: 'Safety, validation, and delivery metrics',
      route: '/mockup-3',
      requirements: [
        'Requirement coverage by flight system · Domain',
        'Defect escape trend by release · Resource',
        'Safety review backlog by owner · Selected'
      ],
      mockData: {
        metrics: [
          { label: 'Open Items', value: 116, delta: '+5%' },
          { label: 'SLA Risk', value: 6, delta: '2 down' },
          { label: 'Flow Health', value: '95%', delta: '+3%' }
        ],
        trendSeries: [
          { label: 'W1', value: 72 },
          { label: 'W2', value: 76 },
          { label: 'W3', value: 81 },
          { label: 'W4', value: 87 },
          { label: 'W5', value: 93 }
        ],
        breakdown: [
          { label: 'Program', value: 35 },
          { label: 'Engineering', value: 30 },
          { label: 'Operations', value: 20 },
          { label: 'Compliance', value: 15 }
        ],
        timeline: [
          { step: 'Intake', eta: '10 min', status: 'done' },
          { step: 'Review', eta: '25 min', status: 'in-progress' },
          { step: 'Approval', eta: '40 min', status: 'queued' }
        ],
        alerts: [
          { severity: 'warning', message: 'Industry Insight Radar: threshold alert requires follow-up' },
          { severity: 'info', message: 'Industry Insight Radar: pipeline synchronized successfully' }
        ],
        records: [
          { id: 'INDUSTRY-INSIGHT-RADAR-103', name: 'Industry Insight Radar primary item', status: 'In Review', owner: 'Product Lead' },
          { id: 'INDUSTRY-INSIGHT-RADAR-104', name: 'Industry Insight Radar validation item', status: 'Pending', owner: 'Ops Manager' },
          { id: 'INDUSTRY-INSIGHT-RADAR-105', name: 'Industry Insight Radar compliance item', status: 'Escalated', owner: 'Compliance Owner' }
        ],
        routeHint: '/mockup-3'
      }
    },
    {
      id: 'detail',
      title: 'Domain Record Canvas',
      role: 'Primary User',
      action: 'As-designed vs as-built traceability',
      route: '/mockup-4',
      requirements: [
        'Change timeline for critical assemblies · Resource',
        'Approval chain for engineering orders · Selected',
        'Certification evidence attachments · Industry'
      ],
      mockData: {
        metrics: [
          { label: 'Open Items', value: 128, delta: '+6%' },
          { label: 'SLA Risk', value: 7, delta: '3 down' },
          { label: 'Flow Health', value: '96%', delta: '+4%' }
        ],
        trendSeries: [
          { label: 'W1', value: 80 },
          { label: 'W2', value: 84 },
          { label: 'W3', value: 89 },
          { label: 'W4', value: 95 },
          { label: 'W5', value: 101 }
        ],
        breakdown: [
          { label: 'Program', value: 35 },
          { label: 'Engineering', value: 30 },
          { label: 'Operations', value: 20 },
          { label: 'Compliance', value: 15 }
        ],
        timeline: [
          { step: 'Intake', eta: '10 min', status: 'done' },
          { step: 'Review', eta: '25 min', status: 'in-progress' },
          { step: 'Approval', eta: '40 min', status: 'queued' }
        ],
        alerts: [
          { severity: 'warning', message: 'Domain Record Canvas: threshold alert requires follow-up' },
          { severity: 'info', message: 'Domain Record Canvas: pipeline synchronized successfully' }
        ],
        records: [
          { id: 'DOMAIN-RECORD-CANVAS-104', name: 'Domain Record Canvas primary item', status: 'In Review', owner: 'Product Lead' },
          { id: 'DOMAIN-RECORD-CANVAS-105', name: 'Domain Record Canvas validation item', status: 'Pending', owner: 'Ops Manager' },
          { id: 'DOMAIN-RECORD-CANVAS-106', name: 'Domain Record Canvas compliance item', status: 'Escalated', owner: 'Compliance Owner' }
        ],
        routeHint: '/mockup-4'
      }
    }
  ];

  activeScreen = this.screens[0];

  selectScreen(screenId: string): void {
    const matchedScreen = this.screens.find((screen) => screen.id === screenId);
    if (matchedScreen) {
      this.activeScreen = matchedScreen;
    }
  }

  getTrendHeight(value: number): number {
    const maxValue = Math.max(...this.activeScreen.mockData.trendSeries.map((point) => point.value));
    return Math.round((value / maxValue) * 100);
  }

  getBreakdownWidth(value: number): number {
    const maxValue = Math.max(...this.activeScreen.mockData.breakdown.map((item) => item.value));
    return Math.round((value / maxValue) * 100);
  }
}
